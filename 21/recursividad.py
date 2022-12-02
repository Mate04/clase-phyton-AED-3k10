
def numeroImaginario(n):
    num = 1
    for i in range(n):
        num *= n-i
    return num


print(numeroImaginario(int(input('numero imaginario? '))))