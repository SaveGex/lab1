# a) Warunek x < 100 jest prawdziwy, ponieważ x = 1. Program wyświetli:
# pierwszy warunek
# został spełniony
# Znak \n oznacza przejście do nowej linii.
x = 1
if x < 100:
 print("pierwszy warunek \nzostał spełniony")
else:
 print("drugi warunek \nnie został spełniony")

# b)Oba warunki są prawdziwe:
# x < 100, ponieważ 1 < 100;
# y % 3 == 0, ponieważ reszta z dzielenia 3 przez 3 wynosi 0.
# Program wyświetli:
# został spełniony
# pierwszy i drugi warunek
x = 1
y = 3
if x < 100:
    print("został spełniony")
    if y % 3 == 0:
        print("pierwszy i drugi warunek")
    else:
        print("tylko pierwszy warunek")
else:
 print("pierwszy warunek\nnie został spełniony")