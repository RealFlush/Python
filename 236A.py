from sys import stdin
n = stdin.readline().strip()
s=[]
for z in n:
    if z not in s:
        s.append(z)
    else:
        continue
if len(s)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
