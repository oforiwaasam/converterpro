class Kilogram():

    def __init__(self, value) -> None:
        self.value = value

    def to_gram(self):
        return self.value * 1000
    
    def to_kilogram(self):
        return self.value