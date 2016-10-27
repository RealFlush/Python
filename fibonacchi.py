def solution(A):
    l=[]
    chet=[]
    summa=0
    summa1=0
    itog=[]
    l.append(1)
    l.append(2)
    for ch in range(2,A):
        l.append(l[ch-1]+l[ch-2])
    for ev in l:
        if ev%2==0:
            chet.append(ev)
    for su in chet:
        summa+=su
    for x in str(summa):
       itog.append(x)
    for y in itog:
        summa1+=int(y)
    print(summa1)
    return summa1
solution(10)
