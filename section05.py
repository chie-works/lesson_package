# while True:
#     word = input('Enter:')
#     if word == 'OK':
#         break
#     print('next')

# while True:
#     Num = input('Enter:')
#     if Num == '10':
#         break
#     print('next')
# name = input("名前を入力してください: ")
# print("こんにちは,", name)

# ---------------------
# some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:
#     print(i)

# for s in 'abcde':
#     print(s)

# for word in ['My', 'name', 'is', 'MIke']:
#     print(word)

# for word in ['My', 'name', 'is', 'MIke']:
#     if word == 'name':
#         break
#     print(word)

# for word in ['My', 'name', 'is', 'MIke']:
#     if word == 'name':
#         continue
#     print(word)
# ------------------------
# for fruit in ['apple', 'banana', 'orange']:
#     if fruit == 'banana':
#         print('stop eating')
#         break
#     print(fruit)
# else:
#     print('I ate all!')
# ----------------------------
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in num_list:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 3):
#     print(i)

# for i in range(10):
#     print(i, 'Hello')

# for _ in range(10):
#     print('Hello')
# ------------------------
# i = 0
# for fruit in ['apple', 'banana', 'orange']:
#     print(i, fruit)
#     i += 1

# for i, fruit in enumerate(['apple', 'banana', 'orange']):
#     print(i, fruit)
# ------------------------------

# days = ['Mon', 'Tue', 'Wed']
# fruits = ['apple', 'banana', 'orange']
# drinks = ['coffee', 'tea', 'bear']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, fruit, drink)
# ------------------------------

# d = {'x' : 100, 'y':200 }

# for v in d:
#     print(v)

# for k, v in d.items():
#     print(k, ':',v)

# print(d.items())
# ------------------------------
# def say_something():
#     print('Hi')

# say_something()

# # say_something_NG()
# # def say_something_NG():
# #     print('Hi')

# print(type(say_something))

# f = say_something
# f()

# def say_something2():
#     s = 'Hello'
#     return s

# result = say_something2()
# print(result)

# def what_is_this(color):
#     if color == 'red':
#         print('tomato')
#     elif color == 'green':
#         print('green pepper')
#     else:
#         return "I don't know"

# result = what_is_this('red')
# result = what_is_this('green')
# result = what_is_this('pink')
# print(result)
# --------------------------------------
# # Python3.6から以下の書き方ができる
# num: int = 10

# def add_num(a: int, b: int ) -> int:
#     return a + b
# r = add_num(10, 20)
# print(r)

# def add_str(a: str, b: str ) -> str:
#     return a + b
# r = add_str('a', 'b')
# print(r)

# def add_num(a: int, b: int ) -> int:
#     return a + b
# r = add_num('a', 'b')
# print(r)
# -----------------------------------------
# print('=========================')
# def menu(entree, drink, dessert):
#     print(entree)
#     print(drink)
#     print(dessert)

# menu('pizza', 'beer', 'ice')

# def menu(entree, drink, dessert):
#     print('entree = ', entree)
#     print('drink = ', drink)
#     print('dessert = ', dessert)

# menu(entree='pizza', drink='beer', dessert='ice')
# menu(drink='beer', entree='pizza',dessert='ice')
# menu('pizza', drink='beer', dessert='ice')
# menu('beer', entree='pizza',dessert='ice')

# def menu2(entree='carry', drink='wine', dessert='cake'):
#     print('entree = ', entree)
#     print('drink = ', drink)
#     print('dessert = ', dessert)

# menu2()
# menu2(entree='pizza', drink='beer', dessert='ice')
# --------------------------
# def test_func(x, l=[]):
#     l.append(x)
#     return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

# r = test_func(100)
# print(r)

# r = test_func(100)
# print(r)


# def test_func(x, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l

# r = test_func(100)
# print(r)

# r = test_func(100)
# print(r)
# -------------------------
# def say_something(word1, word2, word3):
#     print(word1)
#     print(word2)
#     print(word3)

# say_something('Hi!', 'Mike', 'Nancy')

# def say_something(*args):
#     print(args)
#     for arg in args:
#         print(arg)

# say_something('Hi!', 'Mike', 'Nancy')

# def say_something(word, *args):
#     print(word, args)
#     for arg in args:
#         print(arg)

# say_something('Hi!', 'Mike', 'Nancy')


# def say_something(word, *args):
#     print(word, args)
#     for arg in args:
#         print(arg)

# t = ('Mike', 'Nancy')
# say_something('Hi!', *t)
# -------------------------
# def menu(entree='pizza', drink='wine'):
#     print(entree,drink)

# menu()
# menu(entree='cake', drink='coffee')

# def menu(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)

# menu(entree='cake', drink='coffee')


# def menu(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)
# d = {
#     'entree': 'pizza',
#     'drink': 'beer',
#     'dessert': 'ice' 
# }
# menu(**d)

# def menu(food, *args, **kwargs):
#     print(food)
#     print(args)
#     print(kwargs)

# menu('apple', 'banana', 'orange', entree='cake', drink='coffee')

# def menu(food, **kwargs, *args):
#     print(food)
#     print(args)
#     print(kwargs)

# menu('apple', 'banana', 'orange', entree='cake', drink='coffee')

# -------------------------
# def example_func(param1, param2):
#     """
#     example_func の Docstring
#     :param param1: 説明
#     :param param2: 説明
#     """
#     print(param1, param2)
#     return True

# print(example_func.__doc__)
# help(example_func)
# -------------------------
# def outer(a, b):
#     def plus(c, d):
#         return c + d
#     r1 = plus(a, b)
#     r2 = plus(b, a)
#     print(r1 + r2)

# outer(1, 2)
# -------------------------
# def outer(a, b):

#     def inner():
#         return a + b
    
#     return inner

# print(outer(1, 2))

# def outer(a, b):

#     def inner():
#         return a + b
    
#     return inner

# f = outer(1, 2)
# r = f()
# print(r)

# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius
#     return circle_area

# cal1 = circle_area_func(3.14)
# cal2 = circle_area_func(3.141592)

# print(cal1(10))
# print(cal2(10))


# -------------------------
# def add_num(a, b):
#     return a + b

# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)


# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# def add_num(a, b):
#     return a + b

# f = print_info(add_num)
# r = f(10, 20)
# print(r)


# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# @print_info
# def add_num(a, b):
#     return a + b

# r = add_num(10, 20)
# print(r)

# @print_info
# def sub_num(a, b):
#     return a - b

# r = sub_num(100, 20)
# print(r)


# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print('func:', func.__name__)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return wrapper
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# @print_info
# @print_more
# def add_num(a, b):
#     return a + b

# r = add_num(10, 20)
# print(r)


# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print('func:', func.__name__)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return wrapper
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# def add_num(a, b):
#     return a + b

# f = print_info(print_more(add_num))
# r = f(1000,2000)
# print(r)
# -------------------------
# l = ['Mon', 'tue', 'Wed', 'thu', 'fri', 'sat', 'Sun']

# def change_words(words, func):
#     for word in words:
#         print(func(word))

# def sample_func(word):
#     return word.capitalize()

# change_words(l, sample_func)


# def change_words(words, func):
#     for word in words:
#         print(func(word))

# sample_func= lambda word: word.capitalize()

# change_words(l, lambda word: word.capitalize())
# change_words(l, lambda word: word.lower())
# -------------------------
# l = ['Good morning', 'Good afternoon', 'Good night']

# for i in l:
#     print(i)

# def greeting():
#     yield 'Good morning'
#     yield 'Good afternoon'
#     yield 'Good night'

# for g in greeting():
#     print(g)

# def greeting():
#     yield 'Good morning'
#     yield 'Good afternoon'
#     yield 'Good night'

# g = greeting()
# print(next(g))
# print('@@@@')
# print(next(g))
# print('@@@@')
# print(next(g))


# def counter(num=10):
#     for _ in range(num):
#         yield 'run'

# def greeting():
#     yield 'Good morning'
#     yield 'Good afternoon'
#     yield 'Good night'

# g = greeting()
# c = counter()

# print(next(g))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# print(next(g))
# print(next(c))
# print(next(c))
# print(next(c))

# print(next(g))
# print(next(g))

# -------------------------
# t = (1, 2, 3, 4, 5)
# t2 = (5, 6, 7, 8, 9)

# r = []
# for i in t:
#     r.append(i)

# print(r)

# r = [i for i in t]
# print(r)

# r = []
# for i in t:
#     if i % 2 == 0:
#         r.append(i)

# print(r)

# r = [i for i in t if i % 2 == 0]
# print(r)

# r = []
# for i in t:
#     for j in t2:
#         r.append(i * j)
# print(r)

# r = [i * j  for i in t for j in t2]
# print(r)
# -------------------------
# w = ['Mon', 'Tue', 'Wen']
# f = ['coffee', 'Milk', 'Water']

# d = {}
# for x, y in zip(w, f):
#     d[x] = y

# print(d)

# d = {x: y for x, y in zip(w, f)}
# print(d)
# -------------------------
# s = set()

# for i in range(10):
#     s.add(i)

# print(s)

# s = {i for i in range(10)}
# print(s)

# s = set()

# for i in range(10):
#     if i % 2 == 0:
#         s.add(i)

# print(s)

# s = {i for i in range(10) if i % 2 == 0}
# print(s)
# -------------------------
# def g():
#     for i in range(10):
#         yield i

# g = g()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))

# g = (i for i in range(10))
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))


# g = (i for i in range(10) if i % 2 == 0)
# print(type(g))
# print(next(g))

# for x in g:
#     print(x)

# g = tuple(i for i in range(10))
# print(type(g))
# print(g)
# -------------------------
# """main func doc"""

# animal = 'cat'

# def f():
#     # print('before', animal)
#     animal = "dog"
#     print('local:', animal)
# print('grobal:', animal)
# f()


# animal = 'cat'

# def f():
#     global animal
#     animal = "dog"
#     print('local:', animal)
# print('grobal:', animal)
# f()

# def f():
#     """test func doc"""
#     print(f.__name__)
#     print(f.__doc__)

# print(__name__)
# f()

# def f():
#     print('locals:', locals())

# f()
# print('globals:', globals())

# -------------------------
# l = [1, 2, 3]
# i = 5

# # l[i]

# # del l

# try:
#     l[i]
#     # l[0]
#     # () + l
# except IndexError as ex:
#     print("IndexError: {}".format(ex))
# except NameError as ex:
#     print("NameError: {}".format(ex))
# except Exception as ex:
#     print("Exception: {}".format(ex))
# else:
#     print('done')
# finally:
#     print("clean up")

# -------------------------
# raise IndexError('test error')

class UppercaseError(Exception):
    pass

def check():
    # words = ['apple', 'banana', 'orange']
    words = ['APPLE', 'banana', 'orange']
    for word in words:
        if word.isupper():
            # raise UppercaseError(word)
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')

# check()

# -------------------------
# -------------------------
# -------------------------
