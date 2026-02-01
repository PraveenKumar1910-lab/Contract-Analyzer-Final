import spacy, re
nlp=spacy.load('en_core_web_sm')

def extract_entities(t):
    doc=nlp(t); e={'PARTY':[], 'DATE':[], 'MONEY':[], 'GPE':[]}
    for ent in doc.ents:
        if ent.label_ in ['ORG','PERSON']: e['PARTY'].append(ent.text)
        elif ent.label_=='DATE': e['DATE'].append(ent.text)
        elif ent.label_=='MONEY': e['MONEY'].append(ent.text)
        elif ent.label_=='GPE': e['GPE'].append(ent.text)
    e['MONEY']+=re.findall(r'(₹\s?\d+(?:,\d+)*)',t)
    return {k:list(set(v)) for k,v in e.items()}
