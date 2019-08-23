#!/usr/bin/python3
from random import randint
a=[]
for _ in range(4):
    a.append(list(map(lambda x: int(x),input().split(' '))))
b = [(i,j) for i in range(4) for j in range(4) if a[j][i]==0]
print(b[0][0], b[0][1])
print([2,4, 8][randint(0,2)])
