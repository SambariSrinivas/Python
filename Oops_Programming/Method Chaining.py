class Pizza:

    def __init__(self, name):
        self.name = name
        self.toppings = []

    def add_topping(self, topping):  # Method which returns provides a feasibility to do the method chaining
        self.toppings.append(topping.lower())
        return self

    def display_toppings(self):
        print(f"Pizza with name {self.name} has:")
        for topping in self.toppings:
            print(topping.capitalize())


check_pizza = Pizza('Chicken Pizza')

check_pizza.add_topping("mushrooms") \
    .add_topping("olives") \
    .add_topping("chicken") \
    .display_toppings()