from sys import stdin, stdout
words=[]
new_words=[]
for x in range(0,int(stdin.readline())):
    word = stdin.readline().strip()
    if len(word)<=10:
        new_words.append(word)
    else:
        new_words.append(word[:1]+str(len(word)-2)+word[-1:])

for x in new_words:
    print(x)
