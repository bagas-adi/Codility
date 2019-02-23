
def solution(X, A):
    # write your code in Python 3.6 
    count = set([])
    nil = 0
    for i in range(0,len(A)): 
        count.add(A[i]) 
        if len(count) == X:
            return i 
    else :
        return -1 