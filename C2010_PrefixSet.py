def solution(A):
    # write your code in Python 3.6
    lst = set([])
    SET_NUM = len(set(A))
    for i in range(0,len(A)) :
        lst.add(A[i])
        if(len(lst) == SET_NUM):
            return i