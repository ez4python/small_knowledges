print(type(1))  # <class 'int'>
print(type('python'))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({1, 2, 3}))  # <class 'set'>
print(type({1: 1, 2: 4, 3: 9}))  # <class 'dict'>


def greet():
    return 'Hi'


print(type(greet))  # <class 'function'>


# ----------------------- Polymorphism -----------------------

class Transport:
    def action(self):
        print('Action!')

    def __str__(self):
        return self.__class__.__name__


class Car(Transport):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def action(self):
        print('Ride!')


car = Car('Mers', '222')
car.action()

print(Transport())

# ----------------------- Inheritance -----------------------
