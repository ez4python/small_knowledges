class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return 'Driving'


class Car(Vehicle):
    def drive(self):
        return f'{self.brand} {self.model} is driving!'


car = Car('Toyota', 'Corolla')
print(car.drive())
