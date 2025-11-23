# def hypot (a: float, b: float) -> float:
#     print(f'a = {a}, b = {b}')
#     return (a*a + b*b)**0.5
# print(hypot(4,3))


# def great(name):
#     return f'Привет, {name}!'
# great()

# def hello(name):
#     return f'Hello World, {name}'
# print(hello('Ilya'))

# def great():
#     return f'Hello, {great.name}! You are {great.age} years old.'
# great.name = 'Alice'
# great.age = 20
# print(great())

def called():
    called.time = called.time + 1
    return f'Функция {called.__name__} вызвана {called.time} рвз'
called.time = 0
print(called())
print(called())
