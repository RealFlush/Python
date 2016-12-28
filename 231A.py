from sys import stdin, stdout
n= int(stdin.readline())
summa=0
for z in range(n):
    stroka = [int(y) for y in stdin.readline().split()]
    if stroka.count(1)>stroka.count(0):
        summa+=1
#while n>0 and m>0:
#    n-=a
#    m-=a
#    summa+=1
#    summa1+=1
print(summa)
