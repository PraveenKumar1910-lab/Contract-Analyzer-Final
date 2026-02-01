def classify_obligation(t):
    t=t.lower()
    if 'shall not' in t or 'must not' in t: return 'PROHIBITION'
    if 'shall' in t or 'must' in t: return 'OBLIGATION'
    if 'may' in t: return 'RIGHT'
    return 'NONE'
