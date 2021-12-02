from dataManagement import database, recipe

class User():
    # initial constructor, this is what runs when it is initialized inside of main.py
    def __init__(self, key=None):
        #Establish database connection
        self.database = database.Database()

        #TESTING DATABASE
        # self.database.verifyLogin("maxcolt", "12345")

        # is the user signed in?
        self.signed_in = False

        # user settings
        #both of these default to FALSE
        self.public = False
        self.metric = False

        #user info
        self.username = "Guest"
        self.account_age = "0"  # should probably be an int in the future, but str for example purpose

        #these may not be required, we shall see, it depends on where and how they are implemented
        self.recipes = "None"  # list of keys to recipes in the DB
        self.tools = "None"  # list of strings
        self.pantry = "None"  # list of formatted strings (to include amount + unit)

        # working variables, these do not need to be saved
        self.current_search = ""
        self.open_recipe = recipe.Recipe()

        # timers stored here
        # reference to a thread
        # not implemented yet
        # TODO timers
        self.timers = 0


    # this is purely for demo purposes, it is not intended for Production in any way, nor is it representative of any final product
    def example_login(self):
        self.signed_in = True
        self.username = "Example123"
        self.account_age = "10 months"  # should probably be an int in the future, but str for example purpose
        self.recipes = "chicken and rice\ncorndog\nwaffles\nsloppy joe"  # list of keys to recipes in the DB
        self.tools = "whisk\ncutting board\nblender\ngrill"  # list of strings
        self.pantry = "chicken\nrice\nflour\nground beef"  # list of formatted strings (to include amount + unit)
        # self.permissions = "View and Search for recipes \nCreate recipes\nExecute recipes"  # list of bools
        self.metric = True
        self.public = True

    # this one can probably go?
    def example_guest(self):
        self.signed_in = False
        self.username = "Guest"
        self.account_age = "N/A"  # should probably be an int in the future, but str for example purpose
        self.recipes = ""  # list of keys to recipes in the DB
        self.tools = ""  # list of strings
        self.pantry = ""  # list of formatted strings (to include amount + unit)
        # self.permissions = "View and Search for recipes \nCreate recipes\nExecute recipes"  # list of bools
        self.metric = True
        self.public = False
    # the above two functions should be removed as soon as the proper login stuff is ready


    # create timer, pass an integer for the number of minutes
    # might need to pass the UI element to update it from within the thread
    # TODO timers
    def create_timer(self, time):
        pass


    # here are the getters and setters for all the specific requests that need to be done at any point
    # private functions have __ at the beginning, this means that they are for internal class use only
    def __load_from_db(self):
        pass

    def __save_to_db(self):
        pass

    # these are the function that are acessable publicly
    def logout(self):
        pass

    def login(self, username, password):
        attempt = self.database.verifyLogin(username, password)
        # Loads all information from DB here
        if attempt:
            self.username = username
            self.signed_in = True
            # Returns tuple with (private, measurement_system)
            user_info = self.database.getAccountInfo(username)
            # Flipped in database
            self.public = not user_info[0]
            if user_info[1] == "Metric":
                self.metric = True
            else:
                self.metric = False
            return True
        else:
            return False

    # Tell database to change based on current username
    def change_public(self):
        pass
    # Tell database to change based on current username
    def change_units(self):
        pass


    # should only be called from main.py, handled by the anon_search for panels to interact with it
    def search(self, keyword, keywords=None):
        # if there are no keywords then send an empty list
        if keywords is None:
            keywords = []
        # this value is stored so that panels can show the current search in a textbox hint
        self.current_search = keyword
        # TODO database stuff goes here

