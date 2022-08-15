n = 20
v = n * [0]
for i in range(n):
    v[i] = 3*i
    print(v[i])
print(f'arreglo final = {v}')
print('='*60)
n = 6
v = n * [0]
for i in range(n):
    v[i] = '123'
    print(v[i])
print(f'arreglo final = {v}')
print('='*60)
n = 6
v = n * [0]
for i in range(n):
    v[i] = i
    print(v[i])
print(f'arreglo final = {v}')
print('='*60)
v = [2, 4, 1, 6]
v[0] = v[v[0]] * 3
print('v[0]:', v[0])
print('='*60)
n = 5
a = n * [0]
for i in range(n):
    a[i] = i + 1
    print(a[i])
print(f'punto 1: {a}')

v = n * [0]
for i in range(n-1):
    v[a[i]] = a[i]
    print(v[a[i]])
print(f'punto 2: {v}')
print('='*60)
def comprobar(v):
    n = len(v)-1
    for i in range(n):
        if v[i] > v[i+1]:
            return False
    return True
print(comprobar([3,4,5,6]))
print('='*60)
def generar(v):
    n = len(v)

    ac = 0
    for i in range(n):
        ac += v[i]
    p = ac / n

    c = 0
    for i in range(n):
        if v[i] >= p:
            c += 1

    mp = c * [0]
    idx = 0
    for i in range(n):
        if v[i] >= p:
            mp[idx] = v[i]
            idx += 1

    return mp
print(generar([2,3,4]))