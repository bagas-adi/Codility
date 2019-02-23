# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def cpr(a,b):
    if a == "{" and b == "}":
        return True
    elif a == "[" and b == "]":
        return True
    elif a == "(" and b == ")":
        return True
    else : 
        return False
def solution(S):
    # write your code in Python 3.6
    lst = []
    
    for i in S: 
        if i == "{" or i == "[" or i == "(":
            lst.append(i)
        else :
            if len(lst) == 0:
                return 0
            side = lst.pop()
            if not cpr(side, i):
                return 0 
    if len(lst) != 0:
        return 0
    return 1
    