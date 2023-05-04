#1
# import time
# def b(func):
#     def wrapper(x):
#         while True:
#             print(x)
#             time.sleep(1)
#     return wrapper
# @b
# def a(x):
#     pass
# a(input('Word: '))
import f1 as f1

print()

#2

def f1(func):
    def wrapper(d):
        return func(d)
    return wrapper

@f1
def f(x):
    d = 1
    l = x.split(" ")
    for i in l:
        i = int(i)
        d *= i
    print(f'Добуток чисел: {d}')
    return d
f(input('Введіть числа через пробіл: '))


