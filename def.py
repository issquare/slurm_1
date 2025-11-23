# Именные функции, инструкция def
# def add (x, y):
#     return x + y
# add2 = add(10, 10)
# print(add2)
# print(add(10, 10))


# def newfunc(n):
#     def myfunc(x):
#         return n + x
#     return myfunc
#
# new = newfunc(100)
# print(new(200))


# def func(a, b, c=2):  # c - необязательный аргумент
#     return a + b + c
# print(func(1, 2))
# print(func(1, 2, 3))
# print(func(a=1, b=3))


# Функция также может принимать переменное количество позиционных аргументов, тогда перед именем ставится *. Кортеж.
def func(*args):
    return args
print(func(1, 2, 3, 'hello'))
print(func())
print(func(1))


# Функция может принимать и произвольное число именованных аргументов, тогда перед именем ставится **. Словарь.
# def func(**kwargs):
#     return kwargs
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))