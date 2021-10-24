class Card:

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if 1000 < value < 9999:
            self._value = value

    value = property(get_value, set_value) # Defining a property with getter and setter methods for value variable


SBI_Card = Card(4054)
HDFC_Card = Card(8042)

print(f'SBI Card value is: {SBI_Card.value}')

SBI_Card.value = 1234

print(f'New SBI Card value is: {SBI_Card.value}')
