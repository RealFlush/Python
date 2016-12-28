from sys import stdin
k = int(stdin.readline())
l = int(stdin.readline())
m = int(stdin.readline())
n = int(stdin.readline())
d = int(stdin.readline())
summa=0
if k==1 or l==1 or m==1 or n==1:
    print(d)
else:
    for x in range(1,d+1):
        if x%k==0:
            summa+=1
        elif x%l==0 and x%k!=0:
            summa+=1
        elif x%m==0 and x%l!=0 and x%k!=0:
            summa+=1
        elif x%n==0 and x%m!=0 and x%l!=0 and x%k!=0:
            summa+=1
    print(summa)
