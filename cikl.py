#1) При помощи цикла for выведите чётные числа от 2 до 10.
number = 2
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1