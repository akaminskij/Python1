#Задание1
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

def divide(a, b):
    return a / b
if a == 0 or b == 0:
    print('Нельзя делить на ноль!')
else:
    result = divide(a, b)
    print(result)

#Задание2
def card(**kwargs):
    return f"{kwargs['name']}, {kwargs['lastname']}, год - {kwargs['year']}, телефон - {kwargs['phone']}"
print(card(name = 'Андрей', lastname = 'Каминский', year= 1986, phone = '123456789'))

#Задание3
number = input('Введите три числа через пробел: ')
a, b, c = number.split(' ')
a, b, c = int(a), int(b), int(c)

def my_func():
    list1 = [a, b, c]
    list1.sort()
    return sum(list1[1:])

print(f'Сумма двух больших чисел это: {my_func()}')

#Задание4
def my_func(x, y):
    return x**y

while True:
    x = int(input('Введите число a: '))
    y = int(input('Введите отрицательное число b: '))
    if x > 0 and y < 0:
        print(my_func(x, y))
        break
    else:
        print('Введите правильные числа: ')

#Задание5

result = 0
while True:
    mass = input('Input numbers or "exit": ').split()
    x = 0
    for i in list(mass):
        if i == 'exit':
            exit = True
            break
        x += int(i)
    result += x
    print(result)
    if exit == True:
        break

#Задание6
words = 'test word split'.split(' ')

def int_func(word):
    return word.title()

list1 = []

for word in words:
    list1.append(int_func(word))

print(' '.join(list1))




