import random


class Empleo:
    def __init__(self, id, desc, monto, ciudad, tipo):
        self.id = id
        self.descripcion = desc
        self.monto = monto
        self.ciudad = ciudad
        self.tipo = tipo


def to_string(empleo):
    r = 'ID: ' + str(empleo.id) + ' | ' + \
        'Descripción: ' + empleo.descripcion + ' | ' + \
        'Salario: $' + str(empleo.monto) + ' | ' + \
        'Ciudad: ' + str(empleo.ciudad) + ' | ' + \
        'Tipo de empleo: ' + str(empleo.tipo)
    return r


def generar_empleo_aleatorio():
    r = 'Mirqo', 'Ura', 'Metalúrgica', 'Operador', 'Minero', 'Cuchau'
    id = random.randint(100, 999)
    des = random.choice(r)
    salario = round(random.uniform(50000, 1000000), 2)
    ciudad = random.randint(0, 29)
    tipo = random.randint(0, 19)
    return Empleo(id, des, salario, ciudad, tipo)


def pruebita():
    reg = generar_empleo_aleatorio()
    print(to_string(reg))


if __name__ == '__main__':
    pruebita()
