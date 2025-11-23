for i in range(1, 26):
    #if not i % 5:       # если i кратно 5 (5, 10, 15...)
    if i % 5 == 0:
        print(i)        # выводим число и переходим на новую строку
    else:
        print(i, end=' ')  # иначе выводим число с пробелом без перехода на новую строку (для чисел не кратных 5)



# value = int(input('Введите число: '))  # (например, пользователь ввёл 3)
# count = 0
# for i in range(value):       # i = 0, 1, 2
#     for _ in range(i + 1):   # Сначала выполняется 1 раз, затем 2 раза, потом 3 раза. (Повтор действия нужное кол-во раз)
#         count = count + 1    # Каждый раз count запоминается, увеличивается на 1 и печатается строкой ниже
#         print(count, end=' ')
#     else:
#         print()        # Как только количество повторений внутренноего цикла заканчивается, выполняется переход на новую строку




# from random import randint
# a = randint(1, 10)
# check = False
#
# for i in range(1, 9):
#     b = int(input(f'Число загадано! Попытка №{i}: '))
#     if a > b:
#         print('Не правильно! Загаданное число больше!')
#     elif a < b:
#         print('Не правильно! Загаданное число меньше!')
#     else:
#         print('Вы победили!')
#         break




# from random import randint
#
# secret = randint(0, 10)
#
# print('Число загадано! Попытка №1:')
# user_number = int(input())
# for i in range(2, 9):
#     if secret == user_number:
#         print('Вы победили!')
#         break
#     word_min = 'меньше'
#     word_max = 'больше'
#     if secret > user_number:
#         print(f'Не правильно! Загаданное число {word_max}!')
#         print(f'Попытка №{i}')
#         user_number = int(input())
#     elif secret < user_number:
#         print(f'Не правильно! Загаданное число {word_min}!')
#         print(f'Попытка №{i}')
#         user_number = int(input())
# else:
#     print('Вы проиграли!')



# ЗАДАЧА № 4
# from random import randint
#
# secret = randint(0, 100)
#
# print('Число загадано! Попытка №1:')
# user_number = int(input())
# for i in range(2, 9):
#     if user_number == secret:
#         print("Вы победили!")
#         break
#     word = 'меньше' if user_number > secret else 'больше'
#     print(f'Не правильно! Загаданное число {word}!')
#     print(f'Попытка №{i}')
#     user_number = int(input())
# else:
#     print('Вы проиграли!')



# ЗАДАЧА № 5
# number = 50
# step = 50
# for i in range(1, 9):
#     print(f'Попытка №{i}: ', end='')
#     print(f'Это чисто {number}?')
#     choice = input()
#     step = round(step/2)
#     if choice == '=':
#         print('Ура, я победил!')
#         break
#     elif choice == '-':
#         number = number - step
#     elif choice == '+':
#         number = number + step
# else:
#     print('Я проиграл...')