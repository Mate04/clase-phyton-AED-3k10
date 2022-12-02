import time
def replace_at(string, index, char):
    return string[:index] + char + string[index+1:] 
def printPalabra(cadena,delay=0.05):
    vueltaPalabra = 0
    palabra = ''
    bandera = True
    for i in cadena:
        vuelta = 97
        ascii = ord(i)
        if i not in ' .':
            palabra += '-'
            while ascii+1 != vuelta:
                if vuelta > 123 and bandera:
                    vuelta = 241
                    bandera = False
                elif vuelta > 123 and bandera == False:
                    vuelta = 33
                palabra = replace_at(palabra,vueltaPalabra,chr(vuelta))
                print(palabra)
                time.sleep(delay)
                vuelta += 1
        else:
            palabra += ' '
            time.sleep(delay)
        vueltaPalabra += 1
def main():
    printPalabra('Vamos mumi, te va ir joya.',0.03)
    printPalabra('Te amo <3 mucho mucho',0.03)

if __name__ == "__main__":
    main()