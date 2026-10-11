some_number = -1234

print(*(abs(some_number) // 10**digit_position % 10 for digit_position in range(3)))
