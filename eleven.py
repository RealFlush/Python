# -*- coding: utf-8 -*-
def eleven(chislo):
    l=[]
    s1=0
    s2=0
    for x in str(chislo):
        l.append(x)
    for z in l:
        if l.index(z)%2==0:
            s1+=int(z)
        else:
            s2+=int(z)
    if (s1==s2) or (abs(s2-s1)==11):
        print("Это число делится без остатка на 11")
    else:
        print("Это число не делится на 11 без остатка")
    
eleven(3528040)