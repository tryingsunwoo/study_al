def solution(s):
    a =[]
    for b in range(8):
        a.append(str(b))
        c=''.join(a)
        print(c+''.join(list(reversed(c[:-1]))))
    return a

print(solution(8))

def solution1(s):
    for i in list(range(8)):
        num=""
        for j in list(range(2*1+1)):
            if j<=i:
                num +=str(j)
            else:
                num+=str(2*i-j)
        print(""*(8-i)+num+""*(8-i))
        return i
print(solution1(8))