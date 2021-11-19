from dataManagement import ingredients as ings


class Recipe():
    def __init__(self, owner):
        # a string or int that is a key to a specific user in the users table of the DB
        self.owner = owner
        # refer to the ingredients class
        self.ingredients = 0#ings.Ingredients()
        # "money shot" of the dish storage format TBD
        self.image = ""
        # an identifier for the recipe
        self.title = "" # name
        # a list of strings, in the special string format that is TBD
        self.instructions = ""

        # a list of strings?
        self.tags = ""

        # not sure if should be string, or float
        self.average_rating = ""


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

    # this function is for viewing the recipe as a tile in searches
    # it extends
    def UI(self, parent):
        #picture
        #name
        #rating
        #view
        pass