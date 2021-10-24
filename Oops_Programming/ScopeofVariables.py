class Car:
    def __init__(self, name, year):
        self.name = name
        self._year = year


mycar = Car('Suzuki', 2018)
print(mycar._year)
mycar._year = 2020
print(mycar._year)
