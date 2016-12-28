n, k = list(map(int, input().split()))
summa=1
while k%2==0:
    summa+=1
    k=k//2
print(summa)
