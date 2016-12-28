from sys import stdin, stdout
ch1 = [list(y) for y in stdin.readline()]
ch2 = [list(z) for z in stdin.readline()]
#print(ch1)
itog=''
for item in range(0,len(ch1)-1):
    if ch1[item]==ch2[item]:
        itog+='0'
    else:
        itog+='1'
print(itog)
