n =  int(input())
inter = input()
parazit='ogo'
for i in range(n,-1,-1):
    repl = parazit+(i*'go')
    if repl in inter:
        inter =  inter.replace(repl, '*'*3)
        
print(inter)
