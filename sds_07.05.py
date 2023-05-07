#1
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False
people = People(input('Name: '), int(input('Age: ')))
print(people.is_adult())
print(f"Ім'я: {people.name}, Вік: {people.age}")

#2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def P(self):
        p = 2 * (self.width + self.height)
        return p
    def S(self):
        s = self.width * self.height
        return s
r = Rectangle(int(input('Ширина: ')), int(input('Висота: ')))
print(f'Периметр = {r.P()}(см), Площа = {r.S()}(см)^2')

#3
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def result(self):
        print(f'Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}')
car = Car('Audi', 'RS7', 2023 )
car.result()

#4
class Bank:
    def __init__(self):
        self.customers = []
    def add_customer(self, customer):
        self.customers.append(customer)
        return self.customers
    def get_total_balance(self):
        total_balance = 0
        for customer in self.customers:
            total_balance += customer.get_balance()
        return total_balance
    print('Accounts :')
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(self.name,':', self.balance)
    def get_balance(self):
        return self.balance
bank = Bank()
acc1 = BankAccount('Dima', 1000)
acc2 = BankAccount('Masha', 2000)
acc3 = BankAccount('Oleg', 1500)

bank.add_customer(acc1)
bank.add_customer(acc2)
bank.add_customer(acc3)

print('Total balance:',bank.get_total_balance())







