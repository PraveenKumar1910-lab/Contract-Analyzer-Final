WORDS=['reasonable','best efforts','as applicable','from time to time','material']

def detect_ambiguity(t):
    found=[w for w in WORDS if w in t.lower()]
    return {'terms':found,'score':len(found)}
