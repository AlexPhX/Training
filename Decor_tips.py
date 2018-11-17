from functools import reduce


def logger(func):
    def wrapped(*args, **kwargs):
        print("Запуск wrapped")
        return func(*args, **kwargs)
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


def logger1(param):
    def decorator(func):
        def wrapped(*args, **kwargs):
            print(param)
            return func(*args, **kwargs)
        return wrapped
    return decorator


@logger1("Параметр")
def producter(num_list):
    return reduce(lambda x, y: x * y, num_list)

def first_dec(func):
    def wrapped(*args, **kwargs):
        print("First decorator is called!")
        return func(*args, **kwargs)
    return wrapped


def second_dec(func):
    def wrapped(*args, **kwargs):
        print("Second decorator is called!")
        return func(*args, **kwargs)
    return wrapped

@first_dec
@second_dec
def last_func():
    print("Finaly called!")

print(summator([1, 2, 3, 4]))
print(producter([1, 2, 3, 4]))
last_func()
