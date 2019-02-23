
def solution(A):
    # write your code in Python 3.6
    N = len(A)+1
    total = (N*(N+1))//2
    for i in A:
        total -= i
    return total