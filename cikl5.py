#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#Например, если введено число 3486, то надо вывести число 6843.

number = int(input('Enter number: '))
reverse = ''
while number > 0:
    reverse += str(number % 10)
    number = int(number / 10)
print(reverse)