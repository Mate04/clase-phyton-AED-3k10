import os
import random,string
from prettytable import PrettyTable
from clases import Voto,Candidato
import pickle


def cargarVotos(vec:list,n):
    for i in range(n):
        candidato = random.randint(0,6)
        provincia = random.randint(0,20)
        votante = get_random_alphanumeric_string(random.randint(5,12))
        vec.append(Voto(candidato=candidato,provincia=provincia,votante=votante).getData())

def mostrarVotos(matriz):
    x = PrettyTable()
    x.field_names = ["Num Votante", "Num Provincia", "Votante"]
    x.add_rows(matriz)
    print(x)
def mostrarCandidatos(matriz):
    x = PrettyTable()
    x.field_names = ["Codigo","Nombre"]
    x.add_rows(matriz)
    print(x)
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def generarArchivo(fb,vec:list):
    m = open(fb,'wb')
    for i in vec:
        pickle.dump(i,m)
    m.close()

def leerArchivo(fb):
    if not os.path.exists(fb):
        print('No existe el archivo que buscas')
        return 
    m = open(fb, 'rb')
    t = os.path.getsize(fb)
    x = PrettyTable()
    x.field_names = ["Num Votante", "Num Provincia", "Votante"]
    while m.tell() < t:
        x.add_row(pickle.load(m))
    print(x)
    m.close()