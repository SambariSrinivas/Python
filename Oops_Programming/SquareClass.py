class Square:
    # def __int__(self):
    #     self.length = 5
    #     self.width = 5
    num_of_rooms = 5

    def __init__(self, length=5, width=5):  # parameters will come here
        self.length = length  # defining an ojbect Attribute and then Initializing the same.
        self.width = width

    def area(self):
        return self.length * self.width


defaultSquare = Square()
smallSquare = Square(1, 1)
mediumSquare = Square(10, 10)
BigSquare = Square(20, 20)

print('Big Square length is : {}'.format(BigSquare.length))
print('Area of Default Square is : {}'.format(defaultSquare.area()))
print('Area Big Square is : {}'.format(BigSquare.area()))
