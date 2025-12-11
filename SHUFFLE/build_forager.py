#!/usr/bin/env python3
"""
Corpus Forager: Build megadoc with provenance tracking, pretty citations, and theme indexing.
Outputs: megadoc.md, clean_bibliography.bib, corpus_index.json, forager.html
"""

import os
import re
import json
import hashlib
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

SHUFFLE_DIR = Path("/Users/gaia/ATG 3.0/SHUFFLE/markdown")
OUTPUT_DIR = Path("/Users/gaia/ATG 3.0/SHUFFLE/forager")

# Known author mappings for prettier keys
AUTHOR_MAP = {
    'geertz': 'geertz1973',
    'suchman': 'suchman1987',
    'winograd': 'winograd1986',
    'latour': 'latour1987',
    'karpathy': 'karpathy2025',
    'cheng': 'cheng2018',
    'meadows': 'meadows1999',
    'norman': 'norman1988',
    'dijkstra': 'dijkstra1968',
    'hoare': 'hoare2009',
    'bateson': 'bateson1972',
    'garfinkel': 'garfinkel1967',
    'hutchins': 'hutchins1995',
    'dreyfus': 'dreyfus1992',
    'schon': 'schon1983',
    'bowker': 'bowker1999',
    'star': 'bowker1999',
    'scott': 'scott1998',
    'meyer': 'meyer1992',
    'freire': 'freire1970',
    'papert': 'papert1980',
    'vygotsky': 'vygotsky1978',
}

TOPIC_KEYWORDS = {
    'context_engineering': ['context engineering', 'context window', 'prompt engineering', 'RAG', 'retrieval'],
    'thick_description': ['thick description', 'thin description', 'geertz', 'interpretive', 'ethnography'],
    'situated_cognition': ['situated', 'embodied', 'suchman', 'plans and situated', 'cognition in the wild'],
    'negative_space': ['negative space', 'constraint', 'invalid states', 'type system', 'poka-yoke', 'drakon'],
    'lego_ecosystem': ['lego', 'ldraw', 'modulex', 'bricklink', 'studio', 'digital brick'],
    'worlding': ['worlding', 'ian cheng', 'bob', 'bag of beliefs', 'emissary', 'simulation'],
    'infrastructure': ['infrastructure', 'bowker', 'star', 'classification', 'invisible'],
    'hci': ['human-computer', 'interface', 'affordance', 'norman', 'seamful', 'breakdown'],
    'ai_agents': ['agent', 'agentic', 'llm', 'language model', 'hallucination', 'alignment'],
    'sintering': ['sinter', 'consolidation', 'compression', 'memory', 'forge'],
}

def generate_pretty_key(text: str, seen_keys: set) -> str:
    """Generate a semantic citation key from footnote text."""
    text_lower = text.lower()
    
    # Check for known authors
    for author, key_prefix in AUTHOR_MAP.items():
        if author in text_lower:
            # Extract a title word
            title_match = re.search(r'(?:"|\'|_)([A-Za-z]+)', text)
            title_word = title_match.group(1).lower()[:8] if title_match else ''
            base_key = f"{key_prefix}_{title_word}" if title_word else key_prefix
            break
    else:
        # Extract first author-like word and year
        author_match = re.search(r'^([A-Z][a-z]+)', text)
        year_match = re.search(r'\((\d{4})\)', text)
        
        author = author_match.group(1).lower() if author_match else 'source'
        year = year_match.group(1) if year_match else ''
        
        # Extract a meaningful title word
        title_words = re.findall(r'\b([A-Z][a-z]{4,})\b', text)
        # Skip common words
        skip_words = {'December', 'January', 'Accessed', 'Available', 'Retrieved', 'Google', 'Wikipedia'}
        title_word = ''
        for w in title_words:
            if w not in skip_words and w.lower() != author:
                title_word = w.lower()[:10]
                break
        
        base_key = f"{author}{year}_{title_word}" if title_word else f"{author}{year}"
    
    # Ensure uniqueness
    key = base_key
    counter = 1
    while key in seen_keys:
        key = f"{base_key}_{counter}"
        counter += 1
    
    seen_keys.add(key)
    return key

def extract_footnotes(content: str) -> list:
    """Extract numbered footnotes with their full text."""
    footnotes = []
    # Match patterns like "1. Author (Year)..." at end of document
    pattern = r'^(\d+)\.\s+(.+?)(?=\n\d+\.\s|\n\n\n|\Z)'
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
    for num, text in matches:
        footnotes.append({
            'num': int(num),
            'text': text.strip().replace('\n', ' ')
        })
    return footnotes

def extract_themes(content: str) -> list:
    """Identify themes present in content."""
    content_lower = content.lower()
    themes = []
    for theme, keywords in TOPIC_KEYWORDS.items():
        for kw in keywords:
            if kw in content_lower:
                themes.append(theme)
                break
    return themes

def extract_sections(content: str) -> list:
    """Extract section headers for minimap."""
    sections = []
    for match in re.finditer(r'^(#{1,4})\s+(.+)$', content, re.MULTILINE):
        level = len(match.group(1))
        title = match.group(2).strip()
        sections.append({
            'level': level,
            'title': title,
            'pos': match.start()
        })
    return sections

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Global state
    all_citations = {}  # normalized -> {key, text, sources}
    seen_keys = set()
    megadoc_parts = []
    file_provenance = {}
    theme_index = defaultdict(list)
    section_index = []
    
    print("=" * 60)
    print("CORPUS FORAGER: Building megadoc with provenance")
    print("=" * 60)
    
    # First pass: extract all footnotes and generate unified keys
    print("\n[1/4] Extracting citations from all files...")
    
    file_citations = {}
    for md_file in sorted(SHUFFLE_DIR.glob("*.md")):
        content = md_file.read_text(encoding='utf-8')
        footnotes = extract_footnotes(content)
        file_citations[md_file.name] = footnotes
        
        for fn in footnotes:
            # Normalize for deduplication
            norm = re.sub(r'https?://\S+', '', fn['text'])
            norm = re.sub(r'accessed\s+\w+\s+\d+,?\s+\d{4}', '', norm, flags=re.IGNORECASE)
            norm = re.sub(r'\s+', ' ', norm)[:80]
            
            if norm not in all_citations:
                key = generate_pretty_key(fn['text'], seen_keys)
                all_citations[norm] = {
                    'key': key,
                    'text': fn['text'],
                    'sources': [(md_file.name, fn['num'])]
                }
            else:
                all_citations[norm]['sources'].append((md_file.name, fn['num']))
    
    print(f"   Found {len(all_citations)} unique citations")
    
    # Create citation lookup by (file, num)
    citation_lookup = {}
    for norm, info in all_citations.items():
        for source, num in info['sources']:
            citation_lookup[(source, num)] = info['key']
    
    # Second pass: build megadoc with replaced citations
    print("\n[2/4] Building megadoc with provenance markers...")
    
    current_offset = 0
    for md_file in sorted(SHUFFLE_DIR.glob("*.md")):
        content = md_file.read_text(encoding='utf-8')
        filename = md_file.name
        
        # Extract themes
        themes = extract_themes(content)
        for theme in themes:
            theme_index[theme].append(filename)
        
        # Extract sections for minimap
        sections = extract_sections(content)
        for sec in sections:
            section_index.append({
                'file': filename,
                'level': sec['level'],
                'title': sec['title'],
                'offset': current_offset + sec['pos']
            })
        
        # Replace citation numbers with keys
        def replace_citation(match):
            num = int(match.group(1))
            key = citation_lookup.get((filename, num), f"unknown_{num}")
            return f"[{key}]"
        
        # Replace ^N^ with [key]
        content_replaced = re.sub(r'\^(\d+)\^', replace_citation, content)
        
        # Add provenance header
        provenance_header = f"""
---
<!-- PROVENANCE: {filename} -->
<!-- THEMES: {', '.join(themes)} -->
<!-- IMPORTED: {datetime.now().isoformat()} -->

# 📄 {filename.replace('.md', '')}

"""
        
        megadoc_parts.append(provenance_header + content_replaced)
        
        # Track provenance
        file_provenance[filename] = {
            'themes': themes,
            'sections': len(sections),
            'citations': len(file_citations.get(filename, []))
        }
        
        current_offset += len(provenance_header) + len(content_replaced)
    
    # Write megadoc
    megadoc_path = OUTPUT_DIR / "megadoc.md"
    megadoc_content = "\n\n---\n\n".join(megadoc_parts)
    megadoc_path.write_text(megadoc_content, encoding='utf-8')
    print(f"   Wrote: {megadoc_path} ({len(megadoc_content):,} bytes)")
    
    # Third pass: write clean bibliography
    print("\n[3/4] Writing clean bibliography...")
    
    bib_path = OUTPUT_DIR / "clean_bibliography.bib"
    with open(bib_path, 'w', encoding='utf-8') as f:
        f.write("% Clean Bibliography - Corpus Forager\n")
        f.write(f"% Generated: {datetime.now().isoformat()}\n")
        f.write(f"% Unique entries: {len(all_citations)}\n\n")
        
        for norm, info in sorted(all_citations.items(), key=lambda x: x[1]['key']):
            key = info['key']
            text = info['text']
            sources = info['sources']
            
            # Parse author
            author_match = re.search(r'^([^(,]+)', text)
            author = author_match.group(1).strip()[:60] if author_match else 'Unknown'
            
            # Parse year
            year_match = re.search(r'\((\d{4})\)', text)
            year = year_match.group(1) if year_match else 'n.d.'
            
            # Parse URL
            url_match = re.search(r'https?://[^\s\)\]]+', text)
            url = url_match.group(0).rstrip(']') if url_match else ''
            
            # Clean title
            title = re.sub(r'\[.*?\]\(.*?\)', '', text)
            title = re.sub(r'https?://\S+', '', title)
            title = re.sub(r'accessed.*?\d{4}', '', title, flags=re.IGNORECASE)
            title = re.sub(r'\{\.underline\}', '', title)
            title = title[:100].strip()
            
            f.write(f"@misc{{{key},\n")
            f.write(f"  author = {{{author}}},\n")
            f.write(f"  year = {{{year}}},\n")
            f.write(f"  title = {{{title}}},\n")
            if url:
                f.write(f"  url = {{{url}}},\n")
            f.write(f"  note = {{Sources: {len(sources)} files}}\n")
            f.write("}\n\n")
    
    print(f"   Wrote: {bib_path}")
    
    # Fourth pass: write corpus index
    print("\n[4/4] Writing corpus index...")
    
    index = {
        'generated': datetime.now().isoformat(),
        'stats': {
            'files': len(file_provenance),
            'unique_citations': len(all_citations),
            'total_sections': len(section_index)
        },
        'themes': {k: list(set(v)) for k, v in theme_index.items()},
        'files': file_provenance,
        'sections': section_index[:100],  # First 100 for minimap
        'citations': {
            info['key']: {
                'text': info['text'][:200],
                'sources': [s[0] for s in info['sources'][:5]]
            }
            for norm, info in all_citations.items()
        }
    }
    
    index_path = OUTPUT_DIR / "corpus_index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"   Wrote: {index_path}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files processed: {len(file_provenance)}")
    print(f"Unique citations: {len(all_citations)}")
    print(f"Sections indexed: {len(section_index)}")
    print(f"\nTheme coverage:")
    for theme, files in sorted(theme_index.items(), key=lambda x: -len(x[1])):
        print(f"  {theme}: {len(set(files))} files")
    
    print(f"\nOutputs in: {OUTPUT_DIR}")
    print("  - megadoc.md (unified corpus)")
    print("  - clean_bibliography.bib (deduplicated)")
    print("  - corpus_index.json (for UI)")
    
    return index

if __name__ == "__main__":
    main()
