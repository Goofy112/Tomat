class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):  # Инициализация экземпляра класса
        self._index = index
        self._state = 0

    def grow(self):  # Метод роста помидора
        if self._state < 3:
            self._state += 1

    def is_ripe(self):  # Проверка, спелый ли помидор
        return True if self._state == 3 else False


class TomatoBush:

    def __init__(self, count):  # Инициализация класса плантации помидоров
        self.tomatoes = [Tomato(index) for index in range(count)]

    def grow_all(self):  # Рост всех помидоров на плантации
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):  # Проверка, все ли помидоры спелые
        ripeness = [tomato.is_ripe() for tomato in self.tomatoes]
        if all(ripeness):
            return True

    def give_away_all(self):  # Сбор всего урожая
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):  # Работа садовника
        print('Садовник работает...')
        self._plant.grow_all()  # Рост всех помидоров на плантации
        print('\n'.join(f'Помидор {i._index} находится в состоянии: {Tomato.states[i._state]}' for i in self._plant.tomatoes))  # Вывод текущего состояния каждого помидора на плантации
        print('Садовник закончил работу')

    def harvest(self, count):  # Сбор урожая
        if self._plant.all_are_ripe():  # Проверка, все ли помидоры спелые
            if count > len(self._plant.tomatoes):  # Если запрошено больше помидоров, чем есть на плантации
                print(f'Вы ввели некорректное количество кустов. Всего на текущий момент есть {len(self._plant.tomatoes)} кустов')
            else:
                print(f'{self.name} собирает {count} кустов помидоров...')
                ripe_tomatoes = []
                for tomato in self._plant.tomatoes:  # Сбор со стеблем запрошенного количества спелых помидоров
                    if tomato.is_ripe():
                        ripe_tomatoes.append(tomato)

                        if len(ripe_tomatoes) == count:
                            break

                if len(ripe_tomatoes) == count:
                    print(f'{self.name} собрал {count} спелых помидоров со стеблем и выкинул пустые кусты!')  # Вывод сообщения о сборе и удаление пустых кустов
                    for tomato in ripe_tomatoes:
                        self._plant.tomatoes.remove(tomato)
                else:
                    print(f'У вас недостаточно спелых помидоров для сбора. Сейчас на кустах всего {len(ripe_tomatoes)} спелых помидоров')

        else:
            print('Слишком рано! Ваши помидоры зеленые и не созрели')

    def plant(self, count):  # Посадка новых кустов помидоров
        new_plants = TomatoBush(count)
        self._plant.tomatoes.extend(new_plants.tomatoes)

    def knowledge_base():  # Статический метод, выводящий информацию о выращивании и сборе помидоров
        print('Сбор урожая помидоров должен проходить в момент, когда плод еще зрело-зеленый, а затем дать созреть '
              'вне куста.')


if __name__ == '__main__':
    Gardener.knowledge_base()
    tomato_bush_count = int(input('Сколько кустов помидоров вы хотите вырастить? '))
    bush = TomatoBush(tomato_bush_count)
    gardener_name = input('Как зовут вашего садовника? ')
    gardener = Gardener(gardener_name, bush)

    while True:  # Цикл работы программы
        choice = input('Выберите, что вы хотите сделать (введите цифру):\n1. Работать в саду\n2. Собрать урожай\n3. Посадить новые кусты\n4. Закончить работу\n')

        if choice not in ['1', '2', '3', '4']:  # Проверка на ввод неверного значения
            print('Вы ввели некорректное значение. Попробуйте еще раз')
            continue

        if choice == '1':
            gardener.work()
        elif choice == '2':

            tomato_count = int(input(
                f'Сколько кустов помидоров вы хотите собрать? Количество доступных кустов сейчас: {len(bush.tomatoes)} '))
            gardener.harvest(tomato_count)
        elif choice == '3':
            tomato_count = int(input('Сколько кустов помидоров вы хотите посадить? '))
            gardener.plant(tomato_count)
            print(f'{len(gardener._plant.tomatoes) - tomato_count} кустов уже были посажены ранее')
        elif choice == '4':
            break