how_many_sides = int(input("Podaj liczbę boków: "))

print({3: "trójkąt", 4: "czworokąt"}.get(how_many_sides, "wielokąt" if how_many_sides > 4 else "nieprawidłowa liczba boków"))
