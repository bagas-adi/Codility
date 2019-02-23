def solution(A, B):
    # write your code in Python 3.6
    n = len(B)
    lst= []
    survival = n
    for i in range(0,n):
        if B[i] == 1:
            lst.append(i)
        else :
            if len(lst) != 0:
                if A[lst[-1]] < A[i]:
                    lst.pop()
                else :
                    survival -= 1
            else :
                survival -= 1
    else : 
        if len(lst) >0 :
            survival -= len(lst)
    return survival