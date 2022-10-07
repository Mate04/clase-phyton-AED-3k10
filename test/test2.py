from fractions import Fraction
from prettytable import PrettyTable
x = PrettyTable()
matriz = [[1,2],[3,Fraction(5,10)]]
x.add_rows(matriz.get_string())
x.header = False
preserve_internal_border = False
print(x)
