from functools import reduce, partial


def greeter(person, greeting):
    return "{}, {}!".format(greeting, person)


hier = partial(greeter, greeting="Hi")
helloer = partial(greeter, greeting="Hello")

print(hier("Sam"))
print(helloer("sir"))

print(reduce(lambda x, y: x * y, range(1, 6)))

#Списочное выражение
square_list = [number ** 2 for number in range(10)]
print(square_list)

square_list2 = [number ** 2 for number in range(10) if number % 2 == 0]
print(square_list2)

dict = {num: num ** 2 for num in range(1, 6)}
print(dict)

num_list = range(10)
print(list(zip(num_list,square_list)))
