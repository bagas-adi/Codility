# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def prefix_sum(S):
    n = len(S)
    lst= [] #[0]* (5)
    for i in range(0,n): 
        lst.append(val_s(S[i])) #lst[val_s(S[i])] += 1
    return lst
    
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
    pref = prefix_sum(S) 
    for i in range(0,len(P)): 
        if P[i]-Q[i] != 0 :
            nil_min.append(min(pref[ P[i]:Q[i] ]))
        else :
            nil_min.append(pref[P[i]]) 
    return nil_min 

# -------------------------------------------------------------- FAILED 