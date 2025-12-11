#!/usr/bin/env python3
"""
Citation Extractor and Unifier for SHUFFLE Markdown Files
Extracts all citations, deduplicates by author/title, and generates:
1. A unified citation index (JSON)
2. A shared BibTeX bibliography
3. A citation key mapping for each source file
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

SHUFFLE_DIR = Path("/Users/gaia/ATG 3.0/SHUFFLE/markdown")
OUTPUT_DIR = Path("/Users/gaia/ATG 3.0/SHUFFLE/unified")

def extract_footnotes(content: str) -> dict:
    """Extract numbered footnotes from markdown content."""
    footnotes = {}
    # Match patterns like "1. Author (Year)..." or "1. Title - Source..."
    pattern = r'^(\d+)\.\s+(.+?)(?=\n\d+\.\s|\n\n|\Z)'
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
    for num, text in matches:
        footnotes[int(num)] = text.strip()
    return footnotes

def extract_citation_key(text: str) -> str:
    """Generate a citation key from footnote text."""
    # Try to extract author name and year
    # Pattern: "Author, A. (Year)" or "Author (Year)" or just first significant word
    
    # Look for author patterns
    author_match = re.search(r'^([A-Z][a-z]+(?:,\s*[A-Z]\.?)?)', text)
    year_match = re.search(r'\((\d{4})\)', text)
    
    if author_match:
        author = author_match.group(1).split(',')[0].lower()
    else:
        # Use first word
        words = re.findall(r'[a-zA-Z]+', text)
        author = words[0].lower() if words else 'unknown'
    
    year = year_match.group(1) if year_match else 'nd'
    
    # Extract a keyword from title
    title_words = re.findall(r'[a-zA-Z]{4,}', text)
    keyword = ''
    for w in title_words[1:5]:  # Skip author name
        if w.lower() not in ['accessed', 'december', 'https', 'google', 'books', 'the', 'and', 'for']:
            keyword = w.lower()
            break
    
    return f"{author}{year}{keyword}"

def normalize_citation(text: str) -> str:
    """Normalize citation text for deduplication."""
    # Remove URLs and access dates
    text = re.sub(r'\[.*?\]\(https?://[^\)]+\)', '', text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'accessed\s+\w+\s+\d+,?\s+\d{4}', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\{\.underline\}', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:100]  # First 100 chars for comparison

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    all_citations = {}  # normalized_text -> {key, full_text, sources}
    file_mappings = {}  # filename -> {old_num: new_key}
    
    # Process each markdown file
    for md_file in sorted(SHUFFLE_DIR.glob("*.md")):
        print(f"Processing: {md_file.name}")
        content = md_file.read_text(encoding='utf-8')
        footnotes = extract_footnotes(content)
        
        file_mapping = {}
        for num, text in footnotes.items():
            normalized = normalize_citation(text)
            
            if normalized in all_citations:
                # Already seen this citation
                key = all_citations[normalized]['key']
                all_citations[normalized]['sources'].append(md_file.name)
            else:
                # New citation
                key = extract_citation_key(text)
                # Make key unique if needed
                base_key = key
                counter = 1
                while any(c['key'] == key for c in all_citations.values()):
                    key = f"{base_key}{counter}"
                    counter += 1
                
                all_citations[normalized] = {
                    'key': key,
                    'full_text': text,
                    'sources': [md_file.name]
                }
            
            file_mapping[num] = key
        
        file_mappings[md_file.name] = file_mapping
    
    # Generate outputs
    print(f"\nFound {len(all_citations)} unique citations across {len(file_mappings)} files")
    
    # 1. JSON index
    index = {
        'total_unique': len(all_citations),
        'citations': {c['key']: {'text': c['full_text'], 'used_in': c['sources']} 
                      for c in all_citations.values()},
        'file_mappings': file_mappings
    }
    
    json_path = OUTPUT_DIR / "citation_index.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"Saved: {json_path}")
    
    # 2. BibTeX file (basic entries)
    bib_path = OUTPUT_DIR / "unified_bibliography.bib"
    with open(bib_path, 'w', encoding='utf-8') as f:
        f.write("% Unified Bibliography from SHUFFLE files\n")
        f.write(f"% Generated from {len(file_mappings)} source documents\n")
        f.write(f"% Contains {len(all_citations)} unique entries\n\n")
        
        for norm_text, info in sorted(all_citations.items(), key=lambda x: x[1]['key']):
            key = info['key']
            text = info['full_text']
            
            # Try to parse author and year
            author_match = re.search(r'^([^(]+?)(?:\((\d{4})\))?', text)
            author = author_match.group(1).strip() if author_match else 'Unknown'
            year = re.search(r'\((\d{4})\)', text)
            year = year.group(1) if year else 'n.d.'
            
            # Extract URL if present
            url_match = re.search(r'https?://[^\s\)]+', text)
            url = url_match.group(0) if url_match else ''
            
            f.write(f"@misc{{{key},\n")
            f.write(f"  author = {{{author[:50]}}},\n")
            f.write(f"  year = {{{year}}},\n")
            f.write(f"  title = {{{text[:80].replace('{', '').replace('}', '')}...}},\n")
            if url:
                f.write(f"  url = {{{url}}},\n")
            f.write(f"  note = {{Used in: {', '.join(info['sources'][:3])}}}\n")
            f.write("}\n\n")
    
    print(f"Saved: {bib_path}")
    
    # 3. Mapping report
    report_path = OUTPUT_DIR / "mapping_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Citation Mapping Report\n\n")
        f.write(f"**Total unique citations:** {len(all_citations)}\n\n")
        f.write("## Most-Used Citations\n\n")
        f.write("| Citation Key | Used In (files) |\n")
        f.write("|--------------|----------------|\n")
        
        sorted_by_use = sorted(all_citations.values(), 
                               key=lambda x: len(x['sources']), reverse=True)
        for c in sorted_by_use[:30]:
            f.write(f"| `{c['key']}` | {len(c['sources'])} |\n")
        
        f.write("\n## File-by-File Mappings\n\n")
        for filename, mapping in sorted(file_mappings.items()):
            if mapping:
                f.write(f"### {filename}\n\n")
                f.write("| Old # | New Key |\n")
                f.write("|-------|--------|\n")
                for old, new in sorted(mapping.items()):
                    f.write(f"| ^{old}^ | `{new}` |\n")
                f.write("\n")
    
    print(f"Saved: {report_path}")
    print("\nDone!")

if __name__ == "__main__":
    main()
