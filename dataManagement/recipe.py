from dataManagement import ingredients as ings


class Recipe():
    def __init__(self, owner="DEFAULT"):
        # a string or int that is a key to a specific user in the users table of the DB
        self.owner = owner
        # refer to the ingredients class
        self.ingredients = ings.Ingredients()
        # "money shot" of the dish, should be a string referring to the stored location of the image
        self.image = ""
        # an identifier for the recipe
        self.title = "" # name
        # a list of strings
        self.instructions = []
        # a list of strings
        self.tools = []

        # a list of strings?
        self.tags = ""

        # not sure if should be string, or float
        self.average_rating = ""
        self.number_of_ratings = 0
        self.origin = "empty"

    # return a string to be used in search results
    # size is the available space horizontally for text
    def generate_description(self, size=32):
        rating = "({})".format(self.number_of_ratings)
        temp = int(self.average_rating)

        assert temp <= 5, "incorrect rating value should be 0-5 got: {}".format(temp)
        star = "★"
        unfilled = "☆"

        # rating should be out of five stars
        rating = rating + " " + temp * star + unfilled * (5 - temp)
        #        rating of stars  ^             ^ enough stars to get it to 5

        # the string should be [some number of characters that will fit on the button] +newline+ rating # + stars
        return self.title[:int(size / 2)] + "\n" + rating


    def save(self):
        pass

    def load(self):
        pass

    def create(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass