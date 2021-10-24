class Movie:
    def __init__(self, name, rating):
        self.name = name
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, newRating):
        if isinstance(newRating, float) and 1.0 < newRating < 5.0:
            self._rating = newRating




NewMovie = Movie('Mastro', 4.3)

print(f'{NewMovie.name} rating is {NewMovie.rating}')

NewMovie.rating = 4.8

print(f'{NewMovie.name} new rating is {NewMovie.rating}')
