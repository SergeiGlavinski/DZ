# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def card(a):
#     return print('*' * len(a[:-4]) + a[-4:])
#
# card(input('Введите номер карты: '))

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# def slovo(a):
#     print(a)
#     rev = a[::-1]
#     print(rev)
#     if a == rev:
#         print('Слово палиндром!')
#     else:
#         print('Слово не палиндром!')
# slovo(input('Введите слово: '))

# 3. Решите задачу
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

class Tomato:
    # Стадии созревания помидора
    states = {0: 'Пусто', 1: 'Томаты посажены', 2: 'Зелёные томаты', 3: 'Томаты созрели'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Куст {self._index}: {Tomato.states[self._state]}')

class TomatoBush:
    def __init__(self, kol):
        self.tomates = [Tomato(_index) for _index in range(0, kol)]

    def grow_all(self):
        for tomato in self.tomates:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomates])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def ydob(self):
        print('Садовник ухаживает за кустом ...')
        self._plant.grow_all()
        print('Садовник закончил.')

    def sbor(self):
        print('Садовник собирает урожай ...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Садовник закончил.')
        else:
            print('Томаты ещё не созрели!')

    @staticmethod
    def knowledge_base():
        print('''Чаще всего в средней полосе России собирать 
помидоры начинают в начале или середине августа.''')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Генадий', great_tomato_bush)
    gardener.ydob()
    gardener.ydob()
    gardener.sbor()
    gardener.ydob()
    gardener.sbor()

