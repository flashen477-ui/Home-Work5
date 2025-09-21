import random
import time

class Plant:
    def __init__(self, name):
        self.name = name
        self.water_level = 0

    def to_water(self):
        self.water_level += 1

    def to_loosen(self):
        self.water_level += random.randint(0, 2)

class Game:
    def __init__(self):
        self.plants = []

    def add_plant(self, name):
        plant = Plant(name)
        self.plants.append(plant)

    def play(self):
        print('\nДодайте ваші рослини:')
        while True:
            name = input('Введіть назву рослини (або "старт" щоб почати гру): ')
            if name.lower() == 'старт':
                if not self.plants:
                    print('Додайте хоча б одну рослину!')
                    continue
                break
            if name.strip():
                self.add_plant(name)
                print(f'Рослина "{name}" додана!')
            else:
                print('Будь ласка, введіть назву рослини')

        while self.plants:
            print('\nВаші рослини:')
            for plant in self.plants:
                print(f'{plant.name}: Рівень води {plant.water_level}')

            action = input('''\n\tЩо ви хочете зробити:
                [1] - Полити рослину
                [2] - Розпушити землю
                [3] - Вийти
        Ваш вибір: ''')
            
            if action == '1':
                watering = random.choice(self.plants)
                watering.to_water()
                print(f'Ви полили {watering.name}')
            elif action == '2':
                loosening = random.choice(self.plants)
                loosening.to_loosen()
                print(f'Ви розпушили землю навколо {loosening.name}')
            elif action == '3':
                break
            else:
                print('Не коректний вибір. Спробуйте знову.')

            for plant in self.plants[:]:
                if plant.water_level >= 5:
                    print(f'{plant.name} виріс в гарну рослину!')
                    self.plants.remove(plant)
            'time.sleep(1)'

game = Game()

print('Ласкаво просимо до гри "Рослинництво"')
game.play()

print('До побачення!')