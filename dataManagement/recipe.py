from dataManagement import ingredients as ings
import warnings


class Recipe():
    def __init__(self, owner="DEFAULT"):
        if owner == "DEFAULT":
            warnings.warn("you MUST send an owner argument when creating a new recipe instance")
        # a string or int that is a key to a specific user in the users table of the DB
        self.owner = owner
        # refer to the ingredients class
        self.ingredients = ings.Ingredients()
        # "money shot" of the dish, should be a string referring to the stored location of the image
        self.image = "resources/nofile.png"
        # an identifier for the recipe
        self.title = "" # name
        # a list of strings
        self.instructions = []
        # a list of strings
        self.tools = []
        # number of portions; an int
        self.servings = 0
        # a string eg: '2 hours' or '30 min'
        self.prep_time = ""
        # Number of times the recipe has been done
        self.times_exec = 0

        # a list of strings?
        self.tags = []

        # not sure if should be string, or float
        self.average_rating = 0.0
        self.number_of_ratings = 0
        self.origin = "DEFAULT"

    # return a string to be used in search results
    # size is the available space horizontally for text
    def generate_description(self, size=32):
        if self.title == "end of results":
            return self.title
        else:
            rating = "({})".format(self.number_of_ratings)
            temp = int(self.average_rating)

            assert temp <= 5, "incorrect rating value should be 0-5 got: {}".format(temp)
            star = "★"
            unfilled = "☆"

            # rating should be out of five stars
            rating = rating + " " + temp * star + unfilled * (5 - temp)
            #        rating of stars  ^             ^ enough stars to get it to 5

            # the string should be [some number of characters that will fit on the button] +newline+ rating # + stars
            return self.title[:int(size / 2)] + "\n" + \
                   "makes for {} | prep time {}".format(self.servings, self.prep_time)+ "\n" +\
                   rating

    # should be removed as soon as real data is available
    def example(self):
        self.owner = "DEFAULT"
        self.ingredients = ings.Ingredients()
        self.ingredients.example()
        self.image = "resources/fishandchips.jpg"
        self.title = "Classic Fish and Chips" # name
        self.instructions = ["- Fillet the fish",
                             "- Prepare the oil [TIMER:5min]",
                             "- Batter the fish in egg and breadcrumbs",
                             "- This is an example Recipe, you should not see this recipe!"]
        # a list of strings
        self.tools = ["pot",
                      "bowl",
                      "fork"]

        # a list of strings?
        self.tags = ["English", "Seafood", "Lunch", "Fried", "Eggs"]

        self.servings = 6
        self.prep_time = "30 Min"

        # not sure if should be string, or float
        self.average_rating = 4.5
        self.number_of_ratings = 132
        self.origin = "EXAMPLE"
        return self

    # should be kept once real data is available
    def invalid(self):
        self.owner = "ERROR"
        self.ingredients = ings.Ingredients()
        self.ingredients.example()
        self.image = "resources/nofile.png"
        self.title = "INVALID" # name
        self.instructions = []
        # a list of strings
        self.tools = []
        # a list of strings?
        self.tags = []

        self.servings = 0
        self.prep_time = ""

        # not sure if should be string, or float
        self.average_rating = 0
        self.number_of_ratings = 0
        self.origin = "ERROR"
        return self

    # should be kept once real data is available
    def no_more_results(self):
        self.owner = "ENDOFRESULTS"
        self.ingredients = ings.Ingredients()
        self.ingredients.example()
        self.image = "resources/forkandknife.jpg"
        self.title = "end of results"  # name
        self.instructions = []
        # a list of strings
        self.tools = []
        # a list of strings?
        self.tags = []

        self.servings = 0
        self.prep_time = ""

        # not sure if should be string, or float
        self.average_rating = 0
        self.number_of_ratings = 0
        self.origin = "END"
        return self

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