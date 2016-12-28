from sys import stdin, stdout
string = stdin.readline()
sepa1 = '0'
sepa2 = '1'
my_list1 = max(string.split(sepa1)).strip()
my_list2 = max(string.split(sepa2)).strip()
if len(my_list1)>=7 or len(my_list2)>=7:
    print('YES')
else:
    print('NO')
