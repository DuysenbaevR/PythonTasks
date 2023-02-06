#4. Дано натуральное число. Определить:
# а) количество цифр в нем;
# б) сумму его цифр;
# в) произведение его цифр;
# г) среднее арифметическое его цифр;
# д) сумму квадратов его цифр;
# е) сумму кубов его цифр;
# ж) его первую цифру;
# з) сумму его первой и последней цифр.

number = int(input('Enter number: '))
count = 0
summ = 0
proez = 1
arif = 0
sumkv = 0
sumkub = 0
first = 0
last = int(number % 10)
while number > 0:
    summ += int(number % 10)
    proez *= int(number % 10)
    sumkv += int((number % 10)*(number % 10))
    sumkub += int((number % 10)*(number % 10)*(number % 10))
    count += 1
    first = number % 10
    number = int(number / 10)
arif = summ / count
print(f"количество цифр: {count}")
print(f"сумму цифр: {summ}")
print(f"произведение его цифр: {proez}")
print(f"среднее арифметическое его цифр: {arif}")
print(f"сумму квадратов его цифр: {sumkv}")
print(f"сумму кубов его цифр: {sumkub}")
print(f"его первую цифру: {first}")
print(f"сумму его первой и последней цифр: {last + first}")