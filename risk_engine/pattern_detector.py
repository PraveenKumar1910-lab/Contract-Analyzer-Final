PAT={'UNILATERAL_TERMINATION':['terminate at any time'],'INDEMNITY':['indemnify'],'PENALTY':['penalty'],'AUTO_RENEWAL':['automatically renew'],'NON_COMPETE':['non-compete'],'IP_TRANSFER':['intellectual property'],'ARBITRATION':['arbitration']}

def detect_patterns(t):
    t=t.lower(); return [k for k,v in PAT.items() if any(x in t for x in v)]
