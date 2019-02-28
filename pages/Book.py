
class Book:
    def __init__(self):
        self.name = "Unnamed"
        self.author = "No author"
        self.price = 0.0
        self.stars = 0.0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_stars(self, stars):
        self.stars = stars

    def get_stars(self):
        return self.stars
