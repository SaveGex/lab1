a, b, c = 4, 1, 1

some_digits: list[tuple[str, int]] = list(zip("abc", (a, b, c)))
some_digits.sort(key=lambda item: item[1])

print(some_digits[0][0] + "".join(
    f"{' = ' if previous[1] == current[1] else ' < '}{current[0]}"
    for previous, current in zip(some_digits, some_digits[1:])
))
