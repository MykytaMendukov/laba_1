#1
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def is_adult(self):
#         if self.age > 18:
#             return True
#         else:
#             return False
# people = People(input('Name: '), int(input('Age: ')))
# print(people.is_adult())
# print(f"Ім'я: {people.name}, Вік: {people.age}")

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
