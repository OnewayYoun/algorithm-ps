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


def f1(func):
    def wrapper():
        print('started')
        func()
        print('ended')

    return wrapper


@f1  # 데코레이터 붙이면 f2 = f1(f2)
def f2():
    print('hello')


print(f2)
f2()
