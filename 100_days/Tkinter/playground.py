def add(*args):
    s = 0
    for n in args:
        s += n
    return s


print(add(3, 4, 5, 6))

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs['add']
    n *=kwargs['multiply']
    print (n)
    return n


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw['make']
        self.model= kw['model']

# my_car = Car()#does not work
my_car = Car(make="Nissan", model="GTR")


class Car2:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car2()
print(my_car.model)
my_car = Car2(make="Nissan", model="GTR")
print(my_car.model)