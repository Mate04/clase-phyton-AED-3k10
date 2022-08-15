def es_vocal(car):
    vocales = "aeiouaèìòùAEIOUÀÈÌÒÙ"
    return car in vocales

def es_digito(car):
    if car >= "0" or car <= '9':
        return True
    return False

def calcular_porcentaje(cantidad,total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad*100 / total
    return porcentaje



def principal():


    tiene_M = False
    gFirst = True

    cont_letras = 0

    cont_palabras = 0

    cont_vocales = 0
    cont_digito = 0

    pal_dig = 0
    total_pal = 0
    texto = input("Ingrese su texto a procesar(tiene que finalizar en un punto)")

    for letra in texto:
        if letra != " " and letra != ".":
            cont_letras += 1

            #punto 1
            if es_vocal(letra):
                cont_vocales += 1

            if letra == 'm' or letra == 'M':
                tiene_M = True

            if cont_vocales >= 2 and tiene_M and gFirst:
                cont_palabras += 1
                gFirst = False

            # Punto 2

            if es_digito(letra):
                cont_digito += 1

        else:
            total_pal += 1

            # Punto 2
            if cont_digito > cont_vocales:
                pal_dig += 1

            # Reinicios 1
            tiene_M = False
            gFirst = True

            #Reinicios 2
            cont_vocales = 0
            cont_digito = 0
    porcen = calcular_porcentaje(pal_dig,total_pal)




    print('La cantidad de palabras es: ', cont_palabras)
    print('El porcentaje de palabras con mas digito que vocales es:', porcen)




if __name__ == '__main__':
    principal()