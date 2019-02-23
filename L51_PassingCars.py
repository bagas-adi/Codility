# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def prefix_sum(A,pil):
    n = len(A) 
    p = [0] * n
    wcount = 0
    ecount = 0
    to_west = [0]*n
    to_east = [0]*n
    for i in range(0,n):
        if A[(i+1)*-1] == 0:
            wcount += 1
            to_east[(i+1)*-1] = wcount
        elif A[(i+1)*-1] == 1: 
            to_east[(i+1)*-1] = wcount
        if A[i] == 1 :
            ecount += 1
            to_west[i] = ecount
        elif A[i] == 0 :
            to_west[i] = ecount
    if pil == 0:
        return to_east
    elif pil == 1:
        return to_west
def count_total (pref,x,y):
        return pref[y] - pref[x]
        
def solution(cars):
    total = 0 
    n = len(cars)
    pref = prefix_sum(cars,0)
    pref2 = prefix_sum(cars,1)
    for i in range(0,len(cars)): 
        if cars[i] == 0:
            total += count_total(pref2, i,(n-1))
            # print("0 : ",count_total(pref2, i,(n-1)))
        elif cars[i] == 1:
            total += count_total(pref, i,0)
            # print("1 : ",count_total(pref, i,0))
    total //= 2
    if total > 1000000000 :
        return -1
    else :
        return total