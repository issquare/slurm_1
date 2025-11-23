def my_range(stop: int, start: int, step: int = 1):
    result = []
    while start <= stop:
        result.append(start)
        start = start + step
    return result
print(my_range(stop = 5, start = 0, step = 1))
