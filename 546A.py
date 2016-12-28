from sys import stdin
k,n,w = [int(y) for y in stdin.readline().split()]
summa=0
for x in range(1,w+1):
    summa+=x*k
if (summa-n)<0:
    print(0)
else:
    print(summa-n)
