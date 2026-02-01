import re

def clean_text(t):
    t = re.sub(r'\n+', '\n', t)
    t = re.sub(r'\s+', ' ', t)
    return t.strip()
