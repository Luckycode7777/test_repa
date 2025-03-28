"""Описание для описания"""
"""Еще одно описание для описания. типа комент :)"""


def my_func(x, y):
    return x * y


def new_func(x):
    return x + 12 + 5


def new_func_2(x):
    return 4


def new_func_3(x):
    return x * 'Good'


def new_func_4(x):
    print('I am new!') 

def numz(n):
    def dec(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return dec


@numz(2)
def repeat():
    print('Hello Max')

repeat()
>>>>>>> second

### NEW comment
### NEW commit_1

# 5