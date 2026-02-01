import re

def segment_clauses(text):
    parts = re.split(r'(?=\n\d+\.|\n[A-Z][A-Za-z ]+:)', text)
    return [{'clause_id': f'C{i+1}', 'text': p.strip()} for i,p in enumerate(parts) if len(p.strip())>40]
