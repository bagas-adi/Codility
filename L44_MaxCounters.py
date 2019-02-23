def solution(N, A):
    # write your code in Python 3.6
    count = [0]*(N+1)
    save_max = 0
    for i in range(0,len(A)):
        if A[i] >=1 and A[i] <= N:
            count[A[i]] += 1
        elif A[i] == (N+1): 
            count = [max(count)] * len(count)
    count.pop(0)
    print(count)
    return count