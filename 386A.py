from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
summa=0
if a==0 or b==0 or c==0:
    summa=0
else:
    for x in range(1,a+1):
        if b//2>0 and c//4>0:
            summa+=1
            summa+=2
            summa+=4
            a-=1
            b-=2
            c-=4
            
    print(summa)
