from sys import stdin
line1 = stdin.readline().split('+')
line1[-1] = line1[-1].strip()
#line1=line1.strip()
#line1 = line1.replace('\n','')
line1=sorted(line1)
print("+".join(line1))
#print(line1.replace("","+")[1:-1])
