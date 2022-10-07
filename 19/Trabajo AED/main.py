def busquedaSecuencial(lista:list,palabra:str):
    newList = []
    for i in range(len(lista)):
        car = ''
        lista[i]+= ' '
        for j in lista[i]:
            if j in ' ,':
                if car == palabra:
                    print(i)
                    break
                car =''
            else:
                car += j
    return newList

lista = ["nonprofits,certification,curriculum,react,nodejs,javascript,d3,teachers,community,education,programming,math,learn-to-code,careers","book-series,javascript,training-materials,async,education,programming,es6,book,es2015,learn-to-code,training-providers,closures,prototypes,nonprofits"]

busquedaSecuencial(lista,'nonprofits')