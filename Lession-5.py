#Задание1
with open('files\\les1.txt', 'w', encoding='UTF-8') as les1:
    name = input('Введите ваше имя: ')
    second_name = input('Введите вашу фамилию: ')
    age = input('Введите ваш возраст: ')
    les1.writelines([name + '\n', second_name+ '\n', age+ '\n'])
print('Ввод данных завершен. Файл les1.txt сохранен.')

#Задание2
with open('files\\les2.txt', 'r', encoding='UTF-8') as f:
    file = f.readlines()
    for i, value in enumerate(file):
        len_word = len(value.split(' '))
        print(f'Строка {i+1}, слов {len_word} : {value}')

#Задание3
with open('files\\les3.txt', 'r', encoding='UTF-8') as file:
    all_salary = 0
    print('Сотрудники с окладом менее 20000: ')
    for i,line in enumerate(file):
        name, salary = line.split(' ')
        if int(salary) < 20000:
            print(name, salary)
        all_salary += int(salary)
    print('\nСреднй оклад : ')
    print (all_salary/(i+1))

#Задание4
x = {
    'One':'Один',
    'Two':'Два',
    'Three':'Три',
    'Four':'Четыре',
}

def replace_words(s, words):
    for k, v in words.items():
        s = s.replace(k, v)
    return s

with open('files\\les4.txt', 'r', encoding='UTF-8') as file:
    w_res = open('files\\les4-out.txt', 'w', encoding='UTF-8')
    line = file.readline()
    while line:
        print(replace_words(line, x))
        w_res.writelines(replace_words(line, x))
        line = file.readline()
    w_res.close()

#Задание5
import random
x = [random.randint(0, 100) for el in range(10)]
with open('files\\les5.txt', 'w', encoding='UTF-8') as file:
    file.write(' '.join(str(el) for el in x) + '\n')
    file.write(str(sum(x)))

#Задание6
def clean(clean):
    clean = clean.strip().split(' ')
    clean = sum(map(int, [i.split('(')[0].replace('—', '0') for i in clean]))
    return clean

dict = {}

with open('files\\les6.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
        str2 = line.split(':')
        dict[str2[0]] = clean(str2[1])
    print(dict)

#Задание7
import json

dict = {}
all_profit = 0
with open('files\\les7.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(' ')
        profit = int(line[2]) - int(line[3])
        if profit > 0:
            all_profit += profit
        dict[line[0]] = profit
    dict['avg_profit'] = all_profit/len(lines)

with open('files\\les7.json', 'w') as file:
    json.dump(dict, file)
