# # # Creando un iterador


# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)

# #  Iterando un iterador

# while True:
#     try:
#         Element = next(my_iter)
#         print(Element)
#     except StopIteration:
#         break


# # # Asi trabaja el ciclo for por dentro
# # for elemet in my_list:
# #     print(element)


# class EvenNumbers:

#     """Clase que implenta un iterador
#     de todos los Numeros pares, o los numeros
#     pares hasta un maximo"""

#     def __init__(self, max=None):
#         self.max = max

#     def __iter__(self):
#         self.num = 0
#         return self

#     def __next__(self):
#         if not self.max or self.num <= self.max:
#             result = self.num
#             self.num += 2
#             return result
#         else:
#             raise StopIteration


def my_gen():
    """Un ejemplo de generadores"""

    print('Hello world')
    n = 0
    yield n

    print('Hello heaven')
    n = 1
    yield n

    print('Hello hell')
    n = 2
    yield n


a = my_gen()
print(next(a))  # Hello world!
print(next(a))  # Hello heaven
print(next(a))  # Hello hell
print(next(a))
StopIteration
