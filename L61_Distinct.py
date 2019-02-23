# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    lst= []
    n = len(A)
    A.sort()
    count = 1
    if n > 0:
        for i in range(1,n):
            if A[i-1] != A[i]:
                count += 1
    else :
        return 0
    return count