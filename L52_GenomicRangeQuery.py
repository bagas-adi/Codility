def val_s(i):
    impact = 0
    if i == "A":
        impact = 1
    elif i == "C":
        impact = 2
    elif i == "G":
        impact = 3
    elif i == "T":
        impact = 4
    return impact
    
def solution(S, P, Q):
    impact = 0
    nil_min = []
    for i in range(0,len(P)):
        nil_min.append(min( val_s(S[P[i]]) , val_s(S[Q[i]])) ) 
    return nil_min

# -------------------------------------------------------------- FAILED