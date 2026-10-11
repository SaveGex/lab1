temp = float(input("Podaj temperaturę w °C: "))

# Dla ułamkowych temperatur przedział ciepły zaczyna się powyżej 15°C.
print("mróz" if temp < 0 else "chłodno" if temp <= 15 else "ciepło" if temp <= 25 else "gorąco")
