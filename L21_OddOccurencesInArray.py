
def solution(A):
    # write your code in Python 3.6
    dict_ret = {}
    for i in A :
        dict_ret[str(i)] = 0
    for i in A :
        dict_ret[str(i)] += 1
    for i in dict_ret :
        if dict_ret[i] % 2 != 0 :
            return int(i)