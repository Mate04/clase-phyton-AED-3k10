totalDePersonas = int(input("Cuantas personas hay en el pais: "))
personasEnfermas = int(input("Porcentaje de enfermedad: "))

if  personasEnfermas > totalDePersonas:
    print('No se puede calcular el porcentaje de enfermedad por que hay mayor numero de enfermos que habitantes')
else :
    #sacar promedio de personas enfermas en un pais
    promPersonasEnferPais = personasEnfermas / totalDePersonas * 100
    print(promPersonasEnferPais)