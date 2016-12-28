from sys import stdin
n = int(stdin.readline())
summa=0
maximum=0
for z in range(n):
    line = [int(y) for y in stdin.readline().split()]
    summa=summa-line[0]+line[1]
    if maximum<summa:
        maximum = summa
print(maximum)
