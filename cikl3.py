#Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
#если A < B, или в порядке убывания в противном случае. входные данные
#5 9
#выходные данные
#5 6 7 8 9

first = int(input('first: '))
second = int(input('second: '))
if first < second:
    while first <= second:
        print(first)
        first += 1
else:
    while first >= second:
        print(first)
        first -= 1