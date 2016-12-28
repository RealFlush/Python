from sys import stdin, stdout
n,m,a = [int(y) for y in stdin.readline().split()]
if n%a ==0:
    summa=n//a
else:
    summa = n//a+1
if m%a ==0:
    summa1=m//a
else:
    summa1 = m//a+1
"""def func(n,m,a):
    n-=a
    m-=a
    summa+=1
    summa1+=1
    if n<=0 and m<=0:
        return summa*summa1
        print(summa*summa1)
    else:
        func(n,m,a)
func(n,m,a)"""
#while n>0 and m>0:
#    n-=a
#    m-=a
#    summa+=1
#    summa1+=1
print(summa*summa1)
