#Задание1
from sys import argv
script_name, vrbh, stavh, prem = argv
print(f'Зарплата сотрудника ( (Выроботка({vrbh}) * Ставка({stavh}) ) + Премия({prem}) ) =  {(int(vrbh) * int(stavh)) + int(prem)} ')

#Задание2

def max(x):
    for i in range(1, len(x)):
        if x[i] > x[i - 1]:
            yield x[i]

in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
out_list = [el for el in max(in_list)]
print(out_list)

#Задание3
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

#Задание4
def get_unique_digits(l):
    digits_counter = {el: l.count(el) for el in l}
    for el in l:
        if digits_counter[el] == 1:
            yield el

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in get_unique_digits(test_list)])

#Задание5
from functools import reduce

def double(el_p, el):
    return el_p + el

in_list = [digit for digit in range(100, 1001) if digit % 2 == 0]

print(reduce(double, in_list))

#Задание6
from itertools import count

start = int(input('Начальное число: '))
stop = int(input('Конечное число: '))

counter = count(start)

for i in range(start, stop + 1):
    print(next(counter))

from itertools import cycle
cycler = cycle([1, 2, 3])
action = None
print('Нажмите q, чтобы остановиться или любую другую кнопку, чтобы продолжить')
while action != 'q':
    print(next(cycler), end='')
    action = input()

#Задание7
def fact(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num

for el in fact(5):
    print(el)