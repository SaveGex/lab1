some_sides = sorted(float(input(f"Podaj bok {name}: ")) for name in "abc")

if some_sides[0] <= 0 or some_sides[0] + some_sides[1] <= some_sides[2]:
    print("nie można utworzyć trójkąta")
else:
    print({1: "równoboczny", 2: "równoramienny", 3: "różnoboczny"}[len(set(some_sides))])
