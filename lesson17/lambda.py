from functools import reduce
def squared(num): return num * num


print(squared(2))


def addTwo(num): return num + 2


print(addTwo(12))

lambda a, b: a + b


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

addTen(7)
addTwenty(7)

lambda num: num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

list(squared_nums)

lambda num: num % 2 != 0

odd_nums = filter(lambda num: num % 2 != 0, numbers)


total = reduce(lambda acc, curr: acc + curr, numbers)

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
