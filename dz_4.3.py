# ЗАДАЧА 1
def my_range(stop: int, start: int = 0, step: int = 1):
    result = []
    while start <= stop:
        start = start + step
        result.append(start)
    return result
print(my_range(9, 0))



# def greet():
#     return 'Hello World'
# print(greet())

##################################################################

#ЗАДАЧА 2
# def my_range(stop: float, start = 0.0, step = 1.0):
#     while start <= stop:
#         yield start
#         start = start + step
# for i in my_range(9.0, 0.0):
#     print(i)



# def get_apples():
#     apples = []
#     for i in range(11):
#         apples.append(f'Яблоко {i}')
#     return apples
# print(get_apples())

# def gen_apples():
#     for i  in range(11):
#         yield f'Яблоко {i}'
# apples = gen_apples()
# print(next(apples))
# print(next(apples))
# print(next(apples))


# def counter():
#     i = 1
#     while i <= 10:
#         yield i
#         i = i + 1
# for i in counter():
#     print(i)

####################################################################

#ЗАДАЧА 3
# НЕ СТАЛ РЕШАТЬ

####################################################################

#ЗАДАЧА 4
# ХЗ как решать

# def to_string(value, indent=0):
#     result = []
#     if isinstance(value, dict):
#         for key, value in value.items():
#             row = f'\n{" " * indent}{key}: {to_string(value, indent + 2)}'
#             result.append(row)
#     elif isinstance(value, list):
#         result.append(f'array={value}')
#     else:
#         result.append(f'value={value}')
#     return ''.join(result)

####################################################################

#ЗАДАЧА 5
# def is_substring(string: str, sub_string: str):
#     return sub_string in string
#
# #check_str = is_substring('Hello', 'ell')
# #print(check_str)
# print(is_substring('Hello', 'ell'))

####################################################################

#ЗАДАЧА 6
# def to_snake_case(value: str):
#     return '_'.join(value.lower().split())
# print(to_snake_case('heLLo HOW ARE You?'))

####################################################################

#ЗАДАЧА 7

# def is_valid(value: str) -> bool:
#     acc = []
#     for ch in value:
#         if ch == '(':
#             acc.append('(')
#         elif ch == '[':
#             acc.append('[')
#         elif ch == '{':
#             acc.append('{')
#         elif ch == ')':
#             if not acc or acc[-1] != '(':
#                 return False
#             else:
#                 acc.pop()
#         elif ch == ']':
#             if not acc or acc[-1] != '[':
#                 return False
#             else:
#                 acc.pop()
#         elif ch == '}':
#             if not acc or acc[-1] != '{':
#                 return False
#             else:
#                 acc.pop()
#     return len(acc) == 0
#
# value = '()'
# print(is_valid(value))

#ПРОБУЮ САМ РЕШИТЬЗАДАЧУ 7

# def is_valid(value: str):
#     acc = []
#     for ch in value:
#         if ch == '(':
#             acc.append('(')
#         elif ch == '[':
#             acc.append('[')
#         elif ch == '{':
#             acc.append('{')
#         elif ch == ')':
#             if not acc or acc[-1] != '(':
#                 return False
#             else:
#                 acc.pop()
#         elif ch == ']':
#             if not acc or acc[-1] != '[':
#                 return False
#             else:
#                 acc.pop()
#         elif ch == '}':
#             if not acc or acc[-1] != '{':
#                 return False
#             else:
#                 acc.pop()
#     return len(acc) == 0
# value = '((ldsnf()'
# print(f'Результат: {is_valid(value)}')








# def binary_search(arr, item):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(binary_search(my_list, 5))