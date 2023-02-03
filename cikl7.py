#Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Enter number: '))
taq = 0
jup = 0
while number > 0:
    if (number % 10) % 2 == 0:
        jup += 1
    elif (int(number % 10)) % 2 == 1:
        taq += 1
    number = int(number / 10)
print(f" Taq sanlar: {taq}, Jup sanlar: {jup}")