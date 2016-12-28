from sys import stdin
n, k, a, b = list(map(int, input().split()))
ans = ['' for y in range (n)]
rep=1
if a>b:
    ans[1]='G'
    a-=1
else:
    ans[1]='B'
    b-=1

for i in range(2,n+1):
    if rep==k:
        if ans[i-1]=='G' and b<=0 or ans[i-1]!='G' and a<=0:
            print('NO')
            
        elif ans[i-1]=='G':
            b-=1
            ans[i]='B'
        else:
            a-=1
            ans[i]='G'
        rep=1
    if a>b:
        a-=1
        ans[i]='G'
    else:
        b-=1
        ans[i]='B'
    if ans[i]==ans[i+1]:
        rep+=1
print(''.join(ans))    
