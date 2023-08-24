def square(x):
    if not isinstance(x, (int, float)):
        if isinstance(x, str) and x.isdigit():
            x = int(x)
        else:
            raise ValueError('Invalid input:', x)
    return x ** 2

print(square(2))
print(square('a'))

