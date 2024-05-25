def hello():
    print("Hello World!")


hello()


def sum(num1, num2=3):
    if type(num1) is not int or type(num2) is not int:
        return num1 + num2


sum(2, 3)


def multiple_items(*args):
    print(args)
    print(type(args))


def mult_named_items(**kwargs):
    print(kwargs)
