def solution(A):
    # write your code in Python 3.6
    data_ret = []
    if len(A)>1:
        # gimana klo max A gedhe banget?
        count = [0]*(max(A)+1)
        for i in range(0,len(A)):
            if A[i] >0:
                count[A[i]] += 1 
            
        if len(count)>0:
            for i in range(1,len(count)):
                if count[i] == 0:
                    data_ret.append(i)
                    break
            else :
                data_ret.append(max(A)+1)
        else :
            data_ret.append(1)
        # print(count)
        # print(data_ret)
        return min(data_ret)
    else :
        if max(A)-1 > 0:
            return max(A)-1
        elif max(A) > 0:
            return max(A)+1
        else :
            return 1