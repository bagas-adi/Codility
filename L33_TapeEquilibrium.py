
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    P = N-1 
    k = 0 
    temp_P = 0
    tot_P = []
    temp_N = 0
    tot_N = []
    diff = 0
    tot_diff = []
    for i in range(0,N-1):
        temp_P += A[i]
        tot_P.append(temp_P) 
        temp_N += A[(i+1)*-1]
        tot_N.append(temp_N)
    for i in range(0,N-1):
        diff = abs(tot_P[i]-tot_N[(i+1)*-1])
        tot_diff.append(diff)  
    return  min(tot_diff)