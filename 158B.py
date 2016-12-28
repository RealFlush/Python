from sys import stdin, stdout
n= int(stdin.readline())
limit = 4
s = sorted([int(y) for y in stdin.readline().split()])
total = 0
for t in range(len(s)):
    if total+s[t]<limit

