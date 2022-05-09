#Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce: cantidad de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).
#El programa deberá:
#a) TODO: Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.
#b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.
inicio = True
vuelta = 0
while inicio != 0:
    print("Bienvenido al programa de cines")
    vuelta +=1
    recaudacionSinDescuento = 0
    recaudacionConDescuento = 0

    personasSinDescuento = int(input('Cuantos espectadores van a la funcion? sin descuento \n'))
    personasConDescuento = int(input('Cuantos espectadores van a la funcion? con descuento \n'))
    for i in range(personasSinDescuento):
        recaudacionSinDescuento += 75
    for i in range(personasConDescuento):
        recaudacionConDescuento += 50
    TotaldeLaRecaudacion = recaudacionSinDescuento + recaudacionConDescuento
    print('La recaudacion del complejo con las personas sin descuenta es:', recaudacionSinDescuento)
    print('La recaudacion del complejo con las personas con descuenta es:', recaudacionConDescuento)
    print('La recaudacion total del complejo es:', TotaldeLaRecaudacion)
    #sacar el porcentaje de las funciones con descuento y las funciones sin descuento
    porcentajeConDescuento = (recaudacionConDescuento / TotaldeLaRecaudacion) * 100
    porcentajeSinDescuento = (recaudacionSinDescuento / TotaldeLaRecaudacion) * 100
    print('El porcentaje de funciones con descuento es:', porcentajeConDescuento)
    print('El porcentaje de funciones sin descuento es:', porcentajeSinDescuento)
    inicio = int(input('Desea continuar? 0 para salir, 1 para continuar \n'))
if vuelta > 0:
    print('Usted dio', vuelta, 'vueltas')
else:
    print('Usted no hice el programa')