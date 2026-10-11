user_age = int(input("Podaj wiek: "))

print("nieprawidłowy wiek" if user_age < 0 else "co najmniej 18 lat" if user_age >= 18 else "poniżej 18 lat")
