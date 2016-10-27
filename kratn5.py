def solution(A):
    l=[6,2,5,5,4,5,6,3,7,6]
    m=[]
    summa=0
    for x in str(A):
        m.append(x)
    for i in m:
        summa+=l[int(i)]
    print(summa)
    return(summa)
 
solution(7890)
