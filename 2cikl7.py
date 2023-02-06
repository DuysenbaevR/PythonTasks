#7. Напечатать минимальное число, большее 200, которое нацело делится на 17.
number = int(200)
while True:
    if number % 17 == 0:
        break
    number += 1
print(f"Number: {number}")