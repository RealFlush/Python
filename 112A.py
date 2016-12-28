from sys import stdin
line1 = stdin.readline()
line2 = stdin.readline()
if line1.lower()==line2.lower():
    print('0')
#for i in range(len(line1)):
if line1.lower()>line2.lower():
    print('1')
elif line1.lower()<line2.lower():
    print('-1')

