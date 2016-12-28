from itertools import product
from sys import stdin
n = stdin.readline().strip()
summa=0
tipy=0
new_summa=0
if int(n)%4==0:
    print('YES')
elif int(n)%7==0:
    print('YES')
else:

    for a in range(1,len(n)+1):
        types=''
        for x in (product('47', repeat = int(a))):
            types=''
            for ch in x:
                types=types+ch
                tipy+=1
                if int(n)%int(types)==0:
                    new_summa+=1
                    break
                else:
                    summa+=1
    if summa==tipy:
        print('NO')
    if new_summa>0 and new_summa!=tipy:
        print('YES')
