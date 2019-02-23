
def solution(X, Y, D):
    # write your code in Python 3.6
    nil = Y-X
    if nil%D == 0:
        return nil//D
    else :
        return nil//D+1