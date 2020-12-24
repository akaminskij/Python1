# Задание 1:
name = input('Введите ваше имя: ')
age = int(input('Сколько вам лет: '))
print (f'{name}, ваш год рождения: {2020 - age}!')

# Задание 2
clock = int(input('Введите число в секундах: '))
h = clock // 3600
m = (clock % 3600) // 60
s= (clock % 3600) % 60
# str.zfill(self, arg) - дополняет нулями до заданного значения
hour = str.zfill(str(h),2)
min = str.zfill(str(m),2)
sec = str.zfill(str(s),2)
print (f'Time: {hour}:{min}:{sec}')

# Задание 3
n = str(input('n + nn + nnn \nВведите одну любую цифру (от 1 до 9): '))
i = int(n) + int(n+n) + int(n+n+n)
print(i)

# Задание 4
n = str(input('Самая большая цифра в вашем числе это: \nВведите число: '))
max = 0
i = 0
x = 0
while i < len(n):
    m = int(n[i])
    if x <= m:
        x = m
    i += 1
print(f'Самая большая цифра в числе: {x}!')

# Задание 5
profit = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if profit > costs:
    print ('Поздравляю! Вы работаете с прибылью!')
    staff = int(input('давайте узнаем прибыль на каждого сотрудника!\nВведите количество сотрудников фирмы: '))
    profit_per_one = (profit - costs) / staff
    print(f'Прибыль на каждого сотрудника составила {profit_per_one:.2f}!')
else:
    print('Увы. Вы работаете с убытком.')

# Задание 6
a = int(input('Введите результат первого дня, км: '))
b = int(input('Какого результата вы хотите достигнуть?, км: '))
n = 1
while b > a:
    print(f'{n}-й день: {a:.2f} км.')
    a = a * 1.1
    n += 1
print(f'{n}-й день: {a:.2f} км.')
print(f'Ответ: на {n}-й день спортсмен достиг результата - не менее {b} км.')