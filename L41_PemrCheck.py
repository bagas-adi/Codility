
def counting(A):
    N = len(A)
    count = [0] * (max(A) +1)
    for i in range(0,N):
        count[A[i]] += 1
    return count
    
def solution(A):
    # write your code in Python 3.6
    count = counting(A) 
    for i in range(1,len(count)): 
        if count[i] != 1 :
            return 0
    return 1