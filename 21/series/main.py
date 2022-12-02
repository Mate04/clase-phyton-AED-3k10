from modulo import *

def main():
    #genera vector con los generos del archivo txt
    generos = leer_generos('generos.txt')
    #archivo punto 3 txt
    fbTxt = f'{os.path.dirname(os.path.realpath(__file__))}/filtro.txt'
    #archivos csv
    fb = 'series_aed.csv'
    series = []
    #auxiliares
    bandera = False
    archivoBinario = f'{os.path.dirname(os.path.realpath(__file__))}/conteo.dat'
    #Menu de opciones
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            print('generos: ')
            printVect(generos)
        elif opcion == 2:
            leer_series(fb,series,generos)
            printVect(series)
            bandera = True
        elif bandera:
            if opcion == 3:
                a = int(input('duracion minima: '))
                b = int(input('duracion maxima: '))
                filtroMinuto(a,b,series,fbTxt)
            elif opcion == 4:
                conteo = vectorConteos(generos,series)
                genero_int_str(generos,conteo)
                writeBynari(archivoBinario,conteo)
            elif opcion == 5 :
                lectura = readBinary(archivoBinario)
                genero_int_str(generos,lectura)
            elif opcion == 6:
                tit = input('que Titulo de serie quiere buscar: ')
                busquedaTitulo(series,tit)
        elif not bandera:
            print('Porfavor procese de csv a un vector')
        else:
            print('seleccione una opcion valida')
        opcion = menu()
main()
