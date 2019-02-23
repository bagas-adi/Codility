# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    lst_singgung = []
    lst_dalam = []
    hitung = 0
    for i in range(0,n):
        min_border_i = i-A[i]
        max_border_i = i+A[i]
        print("1. A[",i,"] = ",min_border_i,"<",i,"<",max_border_i)
        for j in range(0,n):
            if i == j:
                continue
            min_border_j = j-A[j]
            max_border_j = j+A[j]
            print("2. A[",j,"] = ",min_border_j,"<",j,"<",max_border_j)
            if max_border_i >= max_border_j and min_border_i <= min_border_j:
                print("didalam")
                lst_dalam.append([i,j])
            elif max_border_i >= min_border_j and max_border_i < max_border_j and min_border_i < max_border_j and min_border_i <min_border_j:
                print("tersinggung")
                print([i,j] not in lst_singgung and [j,i] not in lst_singgung) 
                if [i,j] not in lst_singgung and [j,i] not in lst_singgung :
                    lst_singgung.append([i,j]) 
                print(lst_singgung)
            elif max_border_j >= min_border_i and max_border_j < max_border_i and min_border_j < max_border_i and min_border_j <min_border_i:
                print("tersinggung")
                print([i,j] not in lst_singgung and [j,i] not in lst_singgung)
                if [i,j] not in lst_singgung and [j,i] not in lst_singgung :
                    lst_singgung.append([i,j]) 
                    print(lst_singgung)
    print("singgung : ",lst_singgung)
    print("dalam : ",lst_dalam)
    pass
# another test data
# [3,4,1,0,5]
# singgung : [[0, 4], [1, 4]]
# dalam : [[0, 2], [0, 3], [1, 0], [1, 2], [1, 3], [2, 3], [4, 2], [4, 3]]
# total : 10

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    lst_singgung = []
    lst_dalam = []
    hitung = 0
    for i in range(0,n):
        min_border_i = i-A[i]
        max_border_i = i+A[i] 
        for j in range(0,n):
            if i == j:
                continue
            min_border_j = j-A[j]
            max_border_j = j+A[j] 
            if max_border_i >= max_border_j and min_border_i <= min_border_j: 
                lst_dalam.append([i,j])
                hitung += 1
            elif max_border_i >= min_border_j and max_border_i < max_border_j and min_border_i < max_border_j and min_border_i <min_border_j: 
                if [i,j] not in lst_singgung and [j,i] not in lst_singgung :
                    lst_singgung.append([i,j]) 
                    hitung += 1 
            elif max_border_j >= min_border_i and max_border_j < max_border_i and min_border_j < max_border_i and min_border_j <min_border_i: 
                if [i,j] not in lst_singgung and [j,i] not in lst_singgung :
                    lst_singgung.append([i,j]) 
                    hitung += 1 
    return hitung