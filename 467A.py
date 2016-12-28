from sys import stdin
n = int(stdin.readline())
summa=0
for x in range(n):
    line = [int(y) for y in stdin.readline().split()]
    if line[1]-line[0]>=2:
        summa+=1
print(summa)
