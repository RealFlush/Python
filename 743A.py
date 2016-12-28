n, a, b = list(map(int, input().split()))
string = list(map(int, input()))
summa=0
if string[a-1]==string[b-1]:
    summa=0
else:
    summa=1
print(summa)
