from sys import stdin, stdout
n= int(stdin.readline())
x=0
for z in range(n):
    stroka = stdin.readline()
    if '++' in stroka:
        x+=1
    elif '--' in stroka:
        x-=1
#while n>0 and m>0:
#    n-=a
#    m-=a
#    summa+=1
#    summa1+=1
print(x)
