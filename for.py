# for i in 'Hello World':
#     print(i + ' ', end='')


# fruits = ['Яблоко', 'Банан', 'Вишня', 'Виноград']
# for i in fruits:
#     print(i)


# Операторы break и continue для цикла for работают так же как в цикле while
fruits = ['Ананас', 'Клубника', 'Смородина', 'Арбуз']
for i in fruits:
    print(i)
    if i == 'Смородина':
        break

print('\n')

for i in fruits:
    if i == 'Смородина':
        continue
    print(i)