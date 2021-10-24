# This is an example for class Attribute
# This Class Attribute is being used in instance and getting increased after every instance created

class Movie:
    id = 1

    def __init__(self, title, year):
        self.id = Movie.id
        self.title = title
        self.year = year
        Movie.id = Movie.id + 1


LoveStory = Movie("LoveStroy", 2021)
Mastro = Movie('Mastro', 2021)
Check = Movie('Check', 2019)

print('Check Movie id is : {}'.format(Check.id))
print('Mastro Movie id is : {}'.format(Mastro.id))

