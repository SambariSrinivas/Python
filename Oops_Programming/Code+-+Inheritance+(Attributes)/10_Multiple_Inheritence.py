class Rectangle:

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color


class GUIElement:

    def click(self):
        print("The object was clicked...")


class Button(Rectangle,
             GUIElement):  # Button Class has inherited from Rectangle and GUIElement classes, means this class has multiple parents.

    def __init__(self, length, width, color, text):
        Rectangle.__init__(self, length, width, color)
        self.text = text


submit_button = Button(10, 5, "Blue", "submit")
print(submit_button.click())
