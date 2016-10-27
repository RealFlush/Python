B = input("Input binary: ")
for x in B:
    if ord(x)!=49 and ord(x)!=48:
        print ("Wrong input")
        break
    else:
        I=0
        while B!='':
            I=I*2+(ord(B[0])-ord('0'))
            B=B[1:]
        print(I)
        break
