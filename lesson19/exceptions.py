try:
    print(x)
    if not type(x) is str:
        raise TypeError('Only strings are allowed')
except NameError:
    print('A name error')
except ZeroDivisionError:
    print('A zero error')
except Exception as error:
    print(error)
else:
    print('no errors')
finally:
    print("I'm going to print with or without an error")
