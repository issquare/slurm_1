# if False:
#     print('False')
# else:
#     print('True')


x = 1
if x > 10:
    print('> 10')
elif x == 10:
    print('= 10')
elif x < 5:
    print('< 5')
else:
    print('Иное значение')


# a = int(input())
#
# if a > 10:
#     print ('a > 10')
# elif a < 10:
#     print ('a < 10')
# else:
#     print (f'a = {a}')


# import random
# a = random.randint(1, 3)
#
# b = int(input())
# if a == b:
#     print('Yes!')
# else:
#     print('No!')


# import random
# a = random.randint(1, 3)
#
# b = 0
# while a != b:
#     b = int(input('Введите число от 1 до 3: '))
# else:
#     print('Yes! Вы угадали!')


# import random
# a = random.randint(1, 3)

# while True:
#     b = int(input('Введите чисто от 1 до 3: '))
#     if a == b:
#         print('Yes! Вы угадали!')
#         break
#     else:
#         print('No! Вы не угадали, пробуйте еще.')


# import random
# a = random.randint(1, 3)
#
# b = 0
# while a != b:
#     b = int(input('Введите чисто от 1 до 3: '))
#     if a == b:
#         print('Yes! Вы угадали!')
#         break
#     else:
#         print('No! Вы не угадали, пробуйте еще.')



# import random
# a = random.randint(1, 5)
# guessed = False
#
# for i in range (1, 4):
#     b = int(input(f'Введите число. Попытка №{i}: '))
#     if a == b:
#         print(f'Вы угадали с попытки №: {i}')
#         guessed = True
#         break
# if not guessed: # Если guessed не равно True. Если пользоватеть не узадал.
#     print('Попытки исчерпаны. Вы ничего не угадали.')
