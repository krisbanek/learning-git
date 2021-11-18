fives = []
for number in range(0,101):
    if number % 5 == 0 and number / 5 > 0:
        fives.append(number)
cubics = [number * number * number for number in fives]
print(f" Liczby od 0 do 100 podzielne przez 5: {fives}")
print(f" Sześciany liczb od 0 do 100 podzielnych przez 5: {cubics}")
#test GitHub
print("GitHub jest spoczko")
print("branch jest spoczko")
