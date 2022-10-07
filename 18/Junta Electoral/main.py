
from modulos import cargarVotos,mostrarVotos,mostrarCandidatos,generarArchivo, leerArchivo
import os
def main():
    votos = []
    candidatos = [[0,"Juan"],[1,"Trini"],[2,"Jorge"],[4,"Mateo"],[5,"Katara"],[6,"Tom"]]
    op = 1
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/candidatos.dat'
    while op != 0:
        if op == 1:
            cargarVotos(votos,int(input("cuantos votos quiere cargar ")))
        elif op == 2:
            mostrarVotos(votos)
        elif op == 3:
            mostrarCandidatos(candidatos)
        elif op == 4:
            generarArchivo(fb,votos)
        elif op == 5:
            leerArchivo(fb)
        op = int(input('Cargar mas votos: 1\nMostrar: 2\nMostrar Candidatos: 3\nGenerar Archivo: 4\nMostrar Archivo: 5\nsalir: 0\nOpcion: '))
if __name__ == "__main__":
    main()
