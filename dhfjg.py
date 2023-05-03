#1
def a(func):
    def wrapper(x):
        print(x + 10)
    return wrapper
@a
def b(x):
    pass
b(10)
print()

#2

import time
def time_function(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Time: ', end_time - start_time)
        return result
    return wrapper

@time_function
def ex_function(x):
    time.sleep(2)
ex_function(int(input('Enter number: ')))
print()


#3
import random
def cache(func):
    d = {}
    def wrapper(*args):
        r = func(*args)
        d[args] = r
        return d, r
    return wrapper
@cache
def func(a, b):
    return a * b
print(func(random.randint(1,10),random.randint(1,10)))
print()

#4
import random
def log(func):
    def wrapper(*args, **kwargs):
        l = []
        r = func(*args,**kwargs)
        for i in args:
            l.append(i)
        print(l)
        print(f'{l[0]} * {l[1]} = {r}')
        return r
    return wrapper

@log
def f(a, b):
    return a * b
f(random.randint(1,10), random.randint(1,10))