"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de
tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final
del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

1- Determinar la cantidad de palabras que terminaron en vocal. Por ejemplo, en el texto: “En el mar Dios me escucha.”,
tiene 2 palabras terminadas en vocal.

2- El porcentaje de consonantes y el porcentaje de vocales en todo el texto (tener en cuenta que puede haber otros
caracteres): “La universidad es una etapa mas de la vida entre los 18 y los 25 años.” Contiene 27 consonantes, 23
vocales y 54 caracteres en total.

3- Determinar qué palabra tuvo la mayor cantidad de consonantes del texto y mostrar su número de orden entendiendo que
la primera palabra tiene orden 1. Por ejemplo, en el texto: “Los mandriles de Brasil son material de estudio.”, la
palabra “mandriles” con 6 consonantes es la que más consonantes tiene y su número de orden es 2.

4- Determinar la cantidad de palabras que comenzaron con primera letra de todo el texto y además incluyeron “st”. Por ejemplo, en el texto: “En este parcial estamos evaluando lógica.”, encontramos 2 palabras que cumplen la condición “este” y “estamos”.
"""

def es_vocal(letra):
    vocales = "aeiouAEIOU"
    if letra in vocales:
        return True
    else:
        return False

def es_consonante(letra):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    if letra in consonantes:
        return True
    else:
        return False

def calcular_porcentaje(parcial, total):
    porcentaje = 0
    if total != 0:
        porcentaje = (parcial * 100) / total
    return porcentaje


def main():
    anterior = ""
    letras = palabras = palabra_vocal_final = vocales = consonantes = vocales_palabra = consonantes_palabra = letras_palabra = 0
    mayor = cont_est = pal_comienza_st =contPunto4= 0
    bandera = True
    comienza = tienest = banderaPrimeraLetra= False
    banderaComienzode4 = True
    banderaPunto4 = False
    texto = input("Ingrese texto, termina con '.':")
    texto = texto.lower()
    for letra in texto:
        if letra == " " or letra == ".":
        # Por fuera de la palabra
            palabras += 1
            letras_palabra += letras
            #Punto 1
            if es_vocal(anterior):
                palabra_vocal_final += 1
            # Punto 2
            vocales_palabra += vocales
            consonantes_palabra += consonantes
            # Punto 3
            if bandera == True:
                mayor = consonantes
                posicion = palabras
                bandera = False
            if mayor < consonantes:
                mayor = consonantes
                posicion = palabras
            if comienza and tienest:
                pal_comienza_st += 1
            if banderaPunto4:
                contPunto4 += 1
            #Reiniciar
            vocales = 0
            consonantes = 0
            letras = 0
            comieza = False
            tienest = False
            banderaPrimeraLetra = False
            banderaPunto4 = False
        else:
        # Adentro de la palabra
            letras += 1
            
            # Punto 2
            if es_vocal(letra):
                vocales += 1
            if es_consonante(letra):
                consonantes += 1
            # Punto 4
            if banderaComienzode4:
                primeraLetra = letra
                banderaComienzode4 = False
            if primeraLetra == letra and letras == 1:
                banderaPrimeraLetra = True
            if letras> 0 and banderaPrimeraLetra and anterior == 's' and letra == "t":
                banderaPunto4 = True
            # Punto 1
            anterior = letra

    print("La cantidad de palabras que terminan con una vocal es:", palabra_vocal_final)
    porc_vocales = (vocales_palabra * 100) / letras_palabra
    porc_consonantes = (consonantes_palabra * 100) / letras_palabra
    print("Hay", round(porc_vocales,2),"% de vocales, y", round(porc_consonantes,2), "% de consonantes")
    print("La mayor cantidad de consonantes que hay en una palabra es:", mayor,"La posicion de esta palabra es:", posicion)
    print("Las palabras que comiezan con la primer letra del texto y continuan con 'st' son:", pal_comienza_st)
    print(f'punto 4: {contPunto4}')

if __name__ == "__main__":
    main()