from sys import stdin
a = int(stdin.readline())
b = stdin.readline().strip()
new_word=['*' for y in range(a)]

word = ''
if a<=2:
    new_word=b
else:
    for x in range(a):
        new_word[x]=b[int(len(b))-2]
        new_word[-x-1]=b[int(len(b))-1]
        b = b[:int(len(b))-2]
        if len(b)==0:
            break

word=''.join(str(w) for w in new_word)
print(word)    
