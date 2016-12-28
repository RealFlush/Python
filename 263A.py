from sys import stdin
n1 = [int(y) for y in stdin.readline().split()]
n2 = [int(y) for y in stdin.readline().split()]
n3 = [int(y) for y in stdin.readline().split()]
n4 = [int(y) for y in stdin.readline().split()]
n5 = [int(y) for y in stdin.readline().split()]
row=0
pos=0
for i,x in enumerate(n1):
    if x==1:
        row = 1
        pos = i
for i,x in enumerate(n2):
    if x==1:
        row = 2
        pos = i
for i,x in enumerate(n3):
    if x==1:
        row = 3
        pos = i
for i,x in enumerate(n4):
    if x==1:
        row = 4
        pos = i
for i,x in enumerate(n5):
    if x==1:
        row = 5
        pos = i
print(abs(row-3)+abs(pos-2))
