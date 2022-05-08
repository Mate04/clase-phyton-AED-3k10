num1= int(input('ingrese el primer numero'))
num2= int(input('ingrese el segundo numero'))
num3=int(input('ingrese el tercer valor'))

may = None

if (num1 > num2)and(num1 > num3):
    may=('el numero 1 es el mayor',num1)
else:
    may=('el numero 1 no es el mayor',num1)

print('em concluision',may)