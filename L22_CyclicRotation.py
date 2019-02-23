def solution(A, K):
    # write your code in Python 3.6
    num = 1
    temp = 0
    while num <= K:
        i = len(A)-1
        while i > 0:
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
            i -= 1
        num += 1
    return A