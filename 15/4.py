from random import randint, random
n = randint(3,6)
a = []
b = []
for i in range(n):
    a.append(randint(1,10))
    b.append(randint(1,10))
print(f'a: {a}'+'\n'+f'b: {b}')
c = []
for i in range(len(a)):
    if a[i] > b[i]:
        c.append(a[i])
    elif b[i] > a[i]:
        c.append(b[i])
    else:
        c.append(a[i]+b[i])
print(f'c: {c}')