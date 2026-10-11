temp_f = float(input("Podaj temperaturę w °F: "))
temp_c = (temp_f - 32) * 5 / 9

print(f"{temp_c:g} °C")
print("mróz" if temp_c < 0 else "chłodno" if temp_c <= 15 else "ciepło" if temp_c <= 25 else "gorąco")
