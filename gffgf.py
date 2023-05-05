#1
import time
def b(func):
    def wrapper(x):
        while True:
            print(x)
            time.sleep(1)
    return wrapper
@b
def a(x):
    pass
a(input('Word: '))

print()

#2

def f1(func):
    def wrapper(*args, **kwargs):
        k = func(*args, **kwargs) + 100
        print(f'Добуток чисел + 100: {k}')
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

print()

#3

def t(func):
    def wrapper(c):
        res = func(c)
        print(f'{c} градусів Цельсія дорувнюють {res} градусів Фаренгейта')
    return wrapper
@t
def temp(c):
    return c * 1.8 + 32
temp(int(input('Введіть температуру: ')))

print()

# #4
import time
def i(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(0.5)
        func(*args, **kwargs)
        end = time.time()
        print('Time: ', end - start)
    return wrapper
@i
def p(a):
    k = 'Так'
    k1 = 'Ні'
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            print(k1)
    else:
        print(k)
print(p(int(input('Enter number: '))))



