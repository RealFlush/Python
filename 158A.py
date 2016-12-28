from sys import stdin
n,k = [int(y) for y in stdin.readline().split()]
summa=0
nul=0
z = [int(y) for y in stdin.readline().split()]
if z[0]==0:
    summa=0
else:
    summa=k
    for t in range(k,n):
        if z[t]==z[k-1] and z[t]>0:
            summa+=1
    for t in range(n):
        if z[t]==0 and t<k:
            nul+=1

print(summa-nul)
