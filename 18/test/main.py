import pickle
import os
fd = '18/test/data.dat'
def genera_archivo(vec,fd):
    #Anbre el archivo para escribir
    m = open(fd, 'wb')

    #recorre el vector
    for i in range(len(vec)):
        #graba el registro en el archivo
        pickle.dump(vec[i], m)
    #cierra el archivo
    m.close()
def muestra_archivo(fd):
    #verifica si existe el archivo o no
    if not os.path.exists(fd):
        print ("el archivo no existe")
        return

    #abre el archivo para leer
    m = open(fd, 'rb')
    #obtiene el tamaño en bytes del archivo
    t = os.path.getsize(fd)
    print(f'son {t} bytes')
    #recorre el archivo, mientras el file pointer (cantidad de bytes) sea menor al tamaño del archivo
    while m.tell() < t:
        #carga en memoria en la variable socio el registro cargado desde el archivo
        socio = pickle.load(m)
        #imprime el socio
        print(socio)

    #cierra el archivo
    m.close()
genera_archivo(['hola que hace'],fd )
muestra_archivo(fd)