class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def find_area(self):
        print((self.base * self.height) / 2)


class RightTriangle(Triangle):
    def display_area(self):
        print(" === Right Triangle Area ===")
        Triangle.find_area(self)  # calling the super class method from child class


right_triangle = RightTriangle(10, 20)
right_triangle.display_area()

right_triangle.find_area()  # calling the super class method from the object
