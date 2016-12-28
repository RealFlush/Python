n = map(int, input().split())
string = input()
sumR=0
sumD=0
for i in string:
    if i=='D':
        sumR+=1
    else:
        sumD+=1

if sumD-sumR>=2:
    print('D')
if sumR-sumD>=2:
    print('R')

            
