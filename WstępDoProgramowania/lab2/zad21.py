some_year = int(input("Podaj rok: "))
is_leap = some_year % 400 == 0 or (some_year % 4 == 0 and some_year % 100 != 0)
print("nieprawidłowy rok" if some_year <= 0 else "rok przestępny" if is_leap else "rok nieprzestępny")
