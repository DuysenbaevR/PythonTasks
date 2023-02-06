#14. Найти наибольший общий делитель двух заданных натуральных чисел, используя алгоритм Евклида.

first = int(input('First: '))
second = int(input('Second: '))

count = 2
while True:
    if first % count == 0 and second % count == 0:
        break
    count += 1
print(f"наибольший общий делитель двух заданных натуральных чисел: {count}")