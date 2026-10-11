some_sides = sorted(float(input(f"Podaj bok {name}: ")) for name in "abc")
can_be_a_triangle = some_sides[0] > 0 and some_sides[0] + some_sides[1] > some_sides[2]
print("można utworzyć trójkąt" if can_be_a_triangle else "nie można utworzyć trójkąta")
