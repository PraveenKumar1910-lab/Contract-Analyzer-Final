from llm.llm_client import call_llm
BAD=['law','act','section','illegal']

def explain_clause(t,l,r):
    p=f'Explain simply. No laws.\nClause:{t}\nRisk:{l}\nReasons:{r}'
    o=call_llm(p)
    return o if not any(b in o.lower() for b in BAD) else 'Explanation omitted.'
