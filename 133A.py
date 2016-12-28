from sys import stdin
line = stdin.readline().replace("'","")
yazyk='HQ9+'

if line.find('H')>=0 or line.find('Q')>=0 or line.find('9')>=0:
    print('YES')
else:
    print('NO')
