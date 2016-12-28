from sys import stdin, stdout
a =  int(stdin.readline())
if a==2:
    print('NO')
elif a%2 !=0:
    print('NO')
else:
    if (a/2)%2!=0:
        if (int(a/2)-1)%2 !=0:
            print('NO')
        elif (a-(int(a/2)-1))%2==0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
    
