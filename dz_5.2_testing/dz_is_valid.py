def is_valid(value: str):
    acc = []
    for ch in value:
        if ch == '(':
            acc.append('(')
        elif ch == '[':
            acc.append('[')
        elif ch == '{':
            acc.append('{')
        elif ch == ')':
            if not acc or acc[-1] != '(':
                return False
            else:
                acc.pop()
        elif ch == ']':
            if not acc or acc[-1] != '[':
                return False
            else:
                acc.pop()
        elif ch == '}':
            if not acc or acc[-1] != '{':
                return False
            else:
                acc.pop()
    return len(acc) == 0
value = '()'
print(f'Результат: {is_valid(value)}')
