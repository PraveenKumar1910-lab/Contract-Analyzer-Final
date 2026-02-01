PTS={'UNILATERAL_TERMINATION':3,'INDEMNITY':3,'PENALTY':2,'AUTO_RENEWAL':3,'NON_COMPETE':3,'IP_TRANSFER':3,'ARBITRATION':2}

def score_clause(pats, obl, amb):
    s=sum(PTS.get(p,0) for p in pats); r=pats[:]
    if obl=='OBLIGATION': s+=2; r.append('One-sided obligation')
    if amb>0: s+=1; r.append('Ambiguous language')
    lvl='HIGH' if s>=4 else 'MEDIUM' if s>=2 else 'LOW'
    return {'level':lvl,'score':s,'reasons':r}
