
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    A.sort()
    for i in range(0,n-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0