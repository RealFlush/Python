n = int(input())
summa=0
l=list([])
while n>0:
    if n%2==0:
        summa+=1
        l.append(2)
        n=n-2
    else:
        summa+=1
        l.append(3)
        n-=3
print(summa)
print(' '.join(str(v) for v in l))
