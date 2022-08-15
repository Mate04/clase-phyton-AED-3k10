ascias = 'aA Bb'
for car in ascias:
    if car in ' ':
        pass
    else:
        print(f'{car}: {ord(car)}')