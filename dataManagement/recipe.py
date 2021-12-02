from dataManagement import ingredients as ings


class Recipe():
    def __init__(self, owner):
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
        self.__origin = "empty"


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