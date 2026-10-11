a, b, c = 1, -3, 2

if a == 0:
    result = 1 if b != 0 else "nieskończenie wiele" if c == 0 else 0
else:
    delta = b * b - 4 * a * c
    result = 2 if delta > 0 else 1 if delta == 0 else 0
print(result)
