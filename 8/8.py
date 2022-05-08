#Desarrolle un programa completo en phyton,
# controlado por menú de opciones, que incluya las siguientes opciones:
# 1) Ingrese el nombre de 3 paises y además ingrese el producto bruto interno de cada uno de ellos.
# Muestre el nombre del país mas rico de los tres (el de mayor producto bruto interno).
# Además, si el mayor producto bruto interno es superior a 150000,
# indique con un mensaje indicando dicha situación.

# 2)  Ingrese por teclado una cadena de caracteres.

# Procese esa cadena a razón de un caracter por vuelta de ciclo, y determine cuántos caracteres eran vocales.
# Además determine cuántos caracteres 's' hubo en dicho texto.
# Por último determine el porcentaje que cada conteo representa sobre el total de letras del texto.

# 3) Terminar el programa



opcion = int(input('1. Agregue la informacion de tres paises \n 2. Cadena de caracteres \n3. Salir \n'))
while opcion != 3:
    may15000 = False
    opcion = int(input('quiere hacer otra operacion? \n 1. Agregue la informacion de tres paises \n 2. Cadena de caracteres \n3. Salir \n'))
    if opcion == 1:
        for i in range(3):
            pais = input('Ingrese el nombre del pais '+str(i+1)+': ')
            productBruto = int(input('Ingres el producto bruto interno del pais '+str(i+1)+': '))
            if i == 0:
                mayorProductoBruto = productBruto
                mayorProductoBrutoPais = pais
            elif productBruto > mayorProductoBruto:
                mayorProductoBruto = productBruto
                mayorProductoBrutoPais = pais
            if mayorProductoBruto > 150000:
                may15000 = True
        if may15000:
            print('El pais mas rico es: ', mayorProductoBrutoPais, ". Con un producto bruto interno de: ", mayorProductoBruto, ". Con un producto bruto interno mayor a 150000 dolares")
        else:
            print('El pais mas rico es: ', mayorProductoBrutoPais, ". Con un producto bruto interno de: ", mayorProductoBruto, "Aunque ningun pais supero 150000 dolares")
    if opcion == 2:
        cadena = input('Ingrese la cadena de caracteres: ')
    if opcion == 3:
        print('Gracias por usar el programa')