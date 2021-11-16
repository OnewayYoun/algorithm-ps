# def f1(func):
#     def wrapper():
#         print('started')
#         func()
#         print('ended')
#
#     return wrapper
#
#
# def f2():
#     print('hello')
#
#
# f1(f2)()
#
# x = f1(f2)
# print(x)
# x()


# def f1(func):
#     def wrapper():
#         print('started')
#         func()
#         print('ended')
#
#     return wrapper
#
#
# @f1  # 데코레이터 붙이면 f2 = f1(f2)
# def f2():
#     print('hello')
#
#
# print(f2)
# f2()


# def f1(func):
#     def wrapper(*args, **kwargs):
#         print('started')
#         func(*args, **kwargs)
#         print('ended')
#
#     return wrapper
#
#
# @f1  # 데코레이터 붙이면 f2 = f1(f2)
# def f2(a, b=9):
#     print(a, b)
#
#
# f2('hi')


# def f1(func):
#     def wrapper(*args, **kwargs):
#         print('started')
#         val = func(*args, **kwargs)
#         print('ended')
#         return val
#
#     return wrapper
#
#
# @f1  # 데코레이터 붙이면 f2 = f1(f2)
# def f2(a, b=9):
#     print(a, b)
#
#
# @f1  # 데코레이터 붙이면 f2 = f1(f2)
# def add(x, y):
#     return x + y
#
#
# f2('hi')
# print()
# print(add(1, 5))


def before_after(func):
    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')

    return wrapper


class Test:
    @before_after
    def decorated_method(self):
        print('run')


t = Test()
t.decorated_method()


#####################################################################
# *args, **kargs

def number_and_name(*args, **kwargs):
    print(args, kwargs)


number_and_name(1, 2, 3, name="홍길동", age=15)
