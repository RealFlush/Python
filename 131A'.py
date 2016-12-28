from sys import stdin
n = stdin.readline().strip()
n_1 = n[1:].strip()
new_string=n[0].upper()
if n.isupper():
    new_string = n.lower()
elif len(n)==1:
    new_string = n.upper()
else:
    for ch in range(1,len(n)):
        if n[0].isupper() and n[ch].islower():
            new_string=n
        elif n[0].islower() and n_1.isupper():
            new_string=new_string+n[ch].lower()
        else:
            new_string = n
print(new_string.strip())

