import random

class Animal:
    def __init__(self, species, name, age, health, hunger, happiness):
        super().__init__()
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
    def grow(self):
        self.age += 1
        self.health = random.randint(0, 8)
        self.hunger = random.randint(0, 8)
        self.happiness = random.randint(0, 8)
        print(f'Ви виростили {self.name}')
    def eat(self):
        if self.hunger <= 6:
            self.health += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
            self.hunger += random.randint(5, 7)
            print(f'Ви пограли з {self.name}')
        else:
            print(self.name, 'не голодний!')
    def play(self):
        if self.happiness <= 6:
            self.health += random.randint(0,5)
            self.happiness += random.randint(5,8)
            self.hunger -= random.randint(3, 5)
            print(f'Ви пограли з {self.name}')
            if self.hunger < 0:
                self.hunger = 0
                print(f'{self.name} терміново потребує їжу!')
        else:
            print(self.name, 'не хоче грати!')
    def __str__(self):
        return f'Species: {self.species}, Name : {self.name}, Age: {self.age},' \
               f' Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}'
class Zoo:
    def __int__(self):
        super().__init__()
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'\n{animal.name} був доданий до Зоопарку')
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f'\n{animal.name} був видалений з Зоопарку')
        else:
            print(f'\n{animal.name} не був знайдений у Зоопарку')
    def feed_all(self):
        for animal in self.animals:
            animal.eat()
    def play_with_all(self):
        for animal in self.animals:
            animal.play()
            if animal.hunger < 0:
                animal.hunger = 0
                print(f'{animal.name} терміново потребує їжу!')
    def grow_all(self):
        for animal in self.animals:
            animal.age += 1
    def __str__(self):
        return '\n'.join([str(animal) for animal in self.animals])

animal0 = Animal('Rat', 'Vovik', 1, 1, 9, 2)
animal1 = Animal('Lion', 'Bobik', 2, 5, 6, 8)
animal2 = Animal('Racoon', 'Jora', 3, 6, 10, 5)
animal3 = Animal('Elephant', 'Volodya', 13, 8, 8, 4)
zoo = Zoo()
zoo.animals = [animal0, animal1, animal2, animal3]

print('Початковий список тварин:')
print(zoo)
animal4 = Animal('Paroot', 'Bobka', 1, 7, 9, 10)

zoo.add_animal(animal4)  #додавання тварини

zoo.remove_animal(animal0) #видалення тварини
print()
animal1.eat() #пограти з Бобіком
animal2.play()  #пограти з Жорою
animal3.grow() #виростити Володимира
animal4.eat() #спробувати покормити Бобку


print(f'\nСписок після змін:')
print(zoo)


def sim(zoo, day):
    name = f'Day_{day}.txt'
    with open(name, 'w') as file:
        file.write(str(zoo))

for i in range(1, 11):
    print(f'Day_{i}.txt')
    sim(zoo, i)
    zoo.grow_all()
    zoo.feed_all()
    zoo.play_with_all()
    print(zoo)
