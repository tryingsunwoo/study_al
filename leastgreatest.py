def solution(n, m):
    a,b=[],[]
    answer=[]
    for x in range(1,n+1):
        if n%x == 0:
            a.append(x)
    for y in range(1,m+1):
        if m%y ==0:
            b.append(y)
    a.sort(reverse=True)
    for dae in a:
        if dae in b:
            answer.append(dae)
            break
    answer.append(n*m/dae)
    return answer