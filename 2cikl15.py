#15. Найти наименьшее общее кратное двух заданных натуральных чисел.

first = int(input('First: '))
second  = int(input('Second: '))
count = first
if first >= second:
    count = second
elif second >= first:
    count = first
while True:
    if count % first == 0 and count % second == 0:
        break
    count += 1
print(f"наименьшее общее кратное двух заданных натуральных чисел: {count}")