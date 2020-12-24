# Задание 1
# spis = [9, 'abc' , 2.56, None, 345, False]
# for x in spis:
#     print(f'{x} - {type(x)}')

# Задание 2
# spis = list(input('Введите строку: '))
# k = 1
# for i in range(len(spis) // 2):
#     a =  len(spis) // 2
#     print(i)
#     spis[k],spis[i] = spis[i],spis[k]
#     k += 2
# print (''.join(spis))

# Задание 3 через list
# month = int(input('Введите месяц: '))
# decade = ['Зима', 'Весна', 'Лето', 'Осень']
# print(decade)
# if month in [1,2,12]:
#     print(f'{month}-й месяц относиться к поре года: {decade[0]}')
# elif month in [3,4,5]:
#     print(f'{month}-й месяц относиться к поре года: {decade[0]}')
# elif month in [6,7,8]:
#     print(f'{month}-й месяц относиться к поре года: {decade[0]}')
# elif month in [9,10,11]:
#     print(f'{month}-й месяц относиться к поре года: {decade[0]}')
# else:
#     print('Такого месяца не существует!')

# Задание 3 через dict
# month_in = int(input('Введите месяц: '))
# year = {
#     'month1' : [[1,2,12], 'Зима'],
#     'month2' : [[3,4,5], 'Весна'],
#     'month3' : [[6,7,8], 'Лето'],
#     'month4' : [[9,10,11], 'Осень']
#     }
# if month_in in year['month1'][0]:
#     print(f'{month_in}-й месяц относиться к поре года: {year["month1"][1]}')
# elif month_in in year['month2'][0]:
#         print(f'{month_in}-й месяц относиться к поре года: {year["month2"][1]}')
# elif month_in in year['month3'][0]:
#         print(f'{month_in}-й месяц относиться к поре года: {year["month3"][1]}')
# elif month_in in year['month4'][0]:
#         print(f'{month_in}-й месяц относиться к поре года: {year["month4"][1]}')
# else:
#     print('Такого месяца не существует!')

# Задание 4
# words = input('Введите слова через пробел')
# x = 1
# for i in words.split():
#     print(f'{x} {i[0:10]}')
#     x+=1

# Задание 5
# raiting = [9, 8, 7, 6, 2, 1, 1]
# while True:
#     raiting = sorted(raiting, reverse=True)
#     raiting = raiting[0:7]
#     print(raiting)
#     new = int(input('Введите число: '))
#     raiting.append(new)

# Задание 6
# pro = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 20000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 20000, 'количество': 7, 'eд': 'шт.'})
#     ]
# anlytic = {'name': [1], 'price': [], 'ps': [], 'ed': []}
# print(pro[1][1])
#
# for i in anlytic:
#     print(i, anlytic[i])









