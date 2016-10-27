def solution(A):
    l=[]
    for ch in A:
        l.append(ch)
    i=0
    itog=0
    print (len(l))
    while i<=len(l)-13:
        summa=1
        for j in range(i,i+13):
            summa = summa*int(l[j])
        if (itog<summa):
            itog=summa
        i+=1
    print(itog)
    return itog
solution("6563443676799999999999996755447687")
