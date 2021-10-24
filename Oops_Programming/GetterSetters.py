# Class with Getter only
class Movie:
    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title


NewMovie = Movie('LoveStory', 4.6)
OldMovie = Movie('Ishq', 4.8)

print(NewMovie.get_title())
print(OldMovie.get_title())


# Class with Getter and Setter both

class Dog:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, newName):
        if isinstance(newName, str):
            self._name = newName
        else:
            print('Enter a Valid Name of The Dog')


Milky = Dog('Milky', 2)

print('Dog Name is : ', Milky.get_name())

Milky.set_name("Miky_Boy")
print('Dog New Name is : ', Milky.get_name())
