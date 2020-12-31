#Задание1
import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def run(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(5)
            elif i == 2:
                time.sleep(3)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.run()

#Задание2
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * self.volume


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(5000, 20, 125)
print(r.mass())

#Задание3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def full_name(self):
        return self.name + ' ' + self.surname

    def total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Петр', 'Зеленов', 'Worker', 80000, 20000)
print(a.full_name())
print(a.position)
print(a.total_income())

#Задание4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} большая для городского авто'
        else:
            return f'Скорость {self.name} хорошая для городского авто'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего авто {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} высокая для рабочего авто'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} принадлежит полиции'
        else:
            return f'{self.name} не принадлежит полиции'

bmw = SportCar(100, 'Красный', 'БМВ', False)
geely = TownCar(30, 'Белый', 'Джили', False)
lada = WorkCar(70, 'Фиолетовый', 'Лада', False)
ford = PoliceCar(110, 'Голубой',  'Форд', True)
print(lada.turn_left())
print(f'{geely.turn_right()}, {bmw.stop()}')
print(f'{lada.go()} со скоростью {lada.speed} - {lada.show_speed()}')
print(f'{lada.name} цвет {lada.color}')
print(f'{bmw.name} принадлежит полиции? {bmw.is_police}')
print(f'{lada.name}  принадлежит полиции? {lada.is_police}')
print(bmw.show_speed())
print(geely.show_speed())
print(ford.police())
print(ford.show_speed())

#Задание5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Рисуем {self.title}'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Рисуем ручкой'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Рисуем карандашом'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Рисуем маркером'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())