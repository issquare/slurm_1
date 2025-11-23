# lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же

# func = lambda x, y: x + y
# print(func(1, 2))


# func = lambda x, y: x + y
# print(func('a', 'b'))


# func = (lambda x, y: x + y) (1, 2)
# print(func)


# func = (lambda x, y: x + y)('a', 'b')
# print(func)


func = lambda *args: args
print(func(1, 2, 3, 4))
