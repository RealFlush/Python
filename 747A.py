n = int(input())
minimum=n
for a in range(1,n+1):
    if n%a!=0:
        continue
    b = int(n/a)
    if b>a:
        continue
    else:
        if abs(b-a)<minimum:
            minimum=b-a
            itog1=int(a)
            itog2=int(b)
print(itog2,itog1)

