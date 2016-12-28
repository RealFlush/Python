from sys import stdin
z = stdin.readline().strip()
word=''
glasn = 'aAoOyYeEuUiI'
for x in z:
    if x in glasn:
        continue
    else:
        word=word+''.join('.'+x)
print(word.lower())

