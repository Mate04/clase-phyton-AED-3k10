def producto(a,b):
    if a == 0 or b == 0:
        return 0
    print(a)
    return a + producto(a,b-1)
print(producto(5,4))