n, m = map(int, input().split())
projectors=0
line=[]
for i in range(n):
    s=input()
    line.append(s)
    try:
        
        
        projectors+=s.count('0',s.index('1'),len(s))
        projectors+=s.count('0',0 ,s.rindex('1'))
    except:
        continue
for i in range(m):
    try:
        s = ''.join([x[i*2] for x in line])
        projectors+=s.count('0',s.index('1'),len(s))
        projectors+=s.count('0',0, s.rindex('1'))
    except:
        continue
print(projectors)

