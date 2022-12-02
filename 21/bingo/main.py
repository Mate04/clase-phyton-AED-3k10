import time
from colores import *
from maquina import *
from modulos import *
from verificadorFinal import *
def main():
    termino = 1
    bolillasSalidas = []
    print('Bienvenido al bingo!!!')
    nombreJugador = input('ingrese el nombre del participante: ')
    n = verificarMazo(int(input('Cuantos cartones quiere tener? elija entre 1 a 5:\n')),1,5,nombreJugador)
    mazoJugador = mazos(n,'\033[31m',True)
    listaDeTachadasJugador = [[]for i in range(n)]
    registroLinea = []
    vuelta = ronda = 0
    #parte MAQUINA
    mazoCompu = mazos(10-n,mostrar=False)
    listadoDeTachadas = mazoCompu[:]
    listaParalelaFila = [[0 for i in range(9)]for i in range(10-n)] 
    listaParalelaColumna = [[0 for i in range(3)]for i in range(10-n)] 
    while termino != 0:
        opcion = menu()
        if opcion == 1:
            if ronda == 3:
                ronda = ronda4()
                if ronda is int:
                    listaDeTachadasJugador.append(ronda)
                    bolillasSalidas.append(ronda)
                else:
                    poco = verificarMazo(int(input('q carton desea reemplazar')),1,n,nombreJugador)
                    mazoJugador[poco] = ronda
            else:    
                ronda +=1
            bolilla = generedadorBolilla(random.randint(1,99),bolillasSalidas)
            bolillasSalidas.append(bolilla)
            time.sleep(0.1)
            print(BLUE+f'Salio el numero {bolilla}'+WHITE)
            verificarBolilla(mazoCompu,bolilla,listadoDeTachadas)
            for i in range(len(listadoDeTachadas)):
                verificarFilaMaquina(listadoDeTachadas[i],listaParalelaFila[i],i)
                verificadorColumnaMaquina(listadoDeTachadas[i],listaParalelaColumna[i],i)
                if termino:
                    termino = verificadorDeBingo(listaParalelaFila[i],listaParalelaFila[i],i)
            
        elif opcion == 2:
            verTodo = input('quiere ver todo los cartones ponga si\ncarton en particular ponga el numero del carton\n')
            if verTodo in 'si':
                for i in range(len(mazoJugador)):
                    print(f'carton {i+1}')
                    printVect(mazoJugador[i])
            else:
                pos = verificarMazo(int(verTodo)-1,0,n,nombreJugador)
                printVect(mazoJugador[pos])
        elif opcion == 3:
            numCarton = verificarMazo(int(input('Que numero de carton fue: ')),1,n,nombreJugador)
            tipo = verificarMazo(int(input('Q tipo de linea columna(1) o fila(2): ')),1,2,nombreJugador)
            if tipo == 1:
                posicion = verificarMazo(int(input('porfavor seleccione la columna donde fue hecho: ')),1,3,nombreJugador)
            else:
                posicion = verificarMazo(int(input('porfavor seleccione la fila donde fue hecho: ')),1,9,nombreJugador)
            registroLinea.append([numCarton-1,tipo,posicion-1])
        elif opcion == 4:
            print('BINGO!!!!')
            termino = 0
        elif opcion == 5:
            numCarton = verificarMazo(int(input('que numero de carton desea usar para tachar una posicion'))-1,0,4,nombreJugador)
            Numero = int(input(f'que numero desea tachar del carton {numCarton+1}: '))
            listaDeTachadasJugador[numCarton].append(Numero)
    print('se verificaran los cartones')
    validacion = verificarCartones(bolillasSalidas,listaDeTachadasJugador)
    while validacion != False or vuelta < len(registroLinea):
        poscion = registroLinea[i]
        validacion = filasTachadas(poscion[1],posicion[2],poscion[0],bolillasSalidas)
main()