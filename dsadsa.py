#1
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")
student = Student('Oleg', 15)
student.info()

#2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print('Area: ',self.radius**2 * 3.14)
circle = Circle(float(input('Enter radius: ')))
circle.area()


#3
class Animal:
    def __init__(self, sound):
        self.sound = sound
Dog = Animal('Гав!')
print(Dog.sound)

#4

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    def deposit(self):
        v = self.balance + b
        return v
    def withdraw(self):
        v = self.balance - b
        return v
nam = input("Введіть ім'я користувача: ")
b = int(input('Введіть суму для взаємодії: '))
bal = int(input('Введіть баланс: '))
bank = BankAccount(bal, nam)
choise = int(input('Оберіть функцію Нарахування / Знаяття 1/2 : '))
while not 1 <= choise <= 2:
    print(f'"{choise}" не відповідає можливим значення функції')
if choise == 1:
    w = bank.deposit()
elif choise == 2:
    w = bank.withdraw()
print(f"Ім'я користувача: {bank.owner}, Кінцевий баланс : {w}")
