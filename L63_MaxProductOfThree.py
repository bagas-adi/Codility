def solution(A):
    # write your code in Python 3.6
    n = len(A)
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])