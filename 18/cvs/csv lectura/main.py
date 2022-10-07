from prettytable import PrettyTable
import csv
import os
fb = f'{os.path.dirname(os.path.realpath(__file__))}/personas.csv'
x = PrettyTable()
x.field_names = ["Nombre","Apellido","Argentina","ciudad"]
with open(fb) as f:
    reader = csv.reader(f)
    for row in reader:
        x.add_row(row)
print(x)