from sys import stdin
n = int(stdin.readline())
rgb = stdin.readline()

summa=0
for x in range(len(rgb)-1):
    try:
        if rgb[x]==rgb[x+1]:
            summa+=1
    except:
        continue
print(summa)
