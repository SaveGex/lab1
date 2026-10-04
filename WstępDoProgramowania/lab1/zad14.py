import math

a = int(input("Podaj bok a [3]: ") or 3)
b = int(input("Podaj bok b [4]: ") or 4)
alfa = int(input("Podaj kat alfa [90]: ") or 90)

if(alfa > 180):
    raise ValueError("Angle cannot exceed 180 degrees")
if(alfa <= 0):
    raise ValueError("Angle cannot be less than 0 degrees")
pole = a * b * math.sin(math.radians(alfa)) / 2

print(f"Pole trójkąta: {pole}")