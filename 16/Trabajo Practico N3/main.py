from modulos import *
def main():
  proyectos = []
  opcion = menu()
  while opcion != 8:
    if opcion== 1:
      print("Cargar Datos ")
      cargar_datos(proyectos)
      input("Enter para continuar...")

    if opcion== 2:
      print("Lista ordenada por Titulo ")
      proy_ord = sort_proy(proyectos)
      mostrar(proy_ord)
      input("Enter para continuar...")
    if opcion== 3:
        punto3(proyectos)
    if opcion== 4:
      punto4(proyectos)
    if opcion == 5:
        proy_por_año = contar_por_año(proyectos)
        mostrar_proy_por_año(proy_por_año)

    if opcion == 6:
      print(f'que filtro desea buscar'+'\n0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go'+WHITE)
      busqueda = int(input('opcion: '))
      punto6(busqueda,proy_ord)
    if opcion == 7:
        proy_por_año = contar_por_año(proyectos)
        mayor = buscar_mayor(proy_por_año)
        mostrar_años_con_mas_proy(mayor, proy_por_año)
    opcion = menu()

if __name__ == "__main__":
    main()
  
