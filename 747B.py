n = int(input())
x  = list(input())
if n%4!=0:
    print('===')
    exit()
countA=int(n/4)
countC=int(n/4)
countG=int(n/4)
countT=int(n/4)
summaA=0
summaC=0
summaG=0
summaT=0
for i in range(n):
    if x[i]=='A':
        summaA+=1
    elif x[i]=='C':
        summaC+=1
    elif x[i]=='G':
        summaG+=1
    elif x[i]=='T':
        summaT+=1
        
for j in range(n):
    if x[j]=='?':
        if summaA!=countA:
            x[j]='A'
            summaA+=1
        elif summaC!=countC:
            x[j]='C'
            summaC+=1
        elif summaG!=countG:
            x[j]='G'
            summaG+=1
        elif summaT!=countT:
            x[j]='T'
            summaT+=1

if (summaA!=countA) or (summaC!=countC) or (summaG!=countG) or (summaT!=countT):
    print('===')
else:  
    print(''.join(x))
