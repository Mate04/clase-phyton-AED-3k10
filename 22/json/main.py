import os
import json
archivo = f'{os.path.dirname(os.path.realpath(__file__))}/data.json'
with open(archivo) as m:
    data = json.load(m)
for i in data:
    if i.get('categoria') != None:
        print(i)