def punto_dos(vec,nom):
    n=len(vec)
    izq=0
    der=n-1
    pos=None
    while izq<=der:
        c=(izq+der)//2
        if vec[c]==nom:
            pos=c
            break
        elif nom>vec[c]:
            der=c-1
        else:
            izq=c+1
    if pos==None:
        print("no se encontro")
        return False
    else:
        print("los datos del articulo son:",vec[pos])
        return True
print(punto_dos([1,3,4,5,6,7,8,9,10],9))