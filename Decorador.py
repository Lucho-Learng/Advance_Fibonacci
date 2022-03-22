# def decorador(func):
#     def envoltura():
#         print("Esto se anade a mi funcion original")
#         func()
#     return envoltura


# @decorador
# def saludos():
#     print("Hola!")


# # saludos = decorador(saludos)

# saludos()


def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibistes un mensaje'


print(mensaje("Lucho"))
