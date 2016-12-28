
n,x =  [int (n) for n in input().split()]
a = [int (n) for n in input().split()]
summa=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]^a[j]==int(x):
            summa+=1
#end = time.time()
print(summa)
#print(end-start)  
  


