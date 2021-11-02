class User():
    # values defined before the __init__ are class variables, they are not intended to be changed in this case
    settings_default = {"Metric": False}

    # initial constructor, this is what runs when it is initialized inside of main.py
    def __init__(self, key=None):
        # is the user signed in?
        self.signed_in = False

        self.username = "Guest"
        self.account_age = "0"  # should probably be an int in the future, but str for example purpose

        #these may not be required, we shall see, it depends on where and how they are implemented
        self.recipes = "None"  # list of keys to recipes in the DB
        self.tools = "None"  # list of strings
        self.pantry = "None"  # list of formatted strings (to include amount + unit)

        # should be converted to a list of Booleans, so that they can be checked against when the permissions are relevant
        self.permissions = "view and search for recipes"  # list of bools
        # loads the default settings to the instance that is running
        self.settings = User.settings_default


    # this is purely for demo purposes, it is not intended for Production in any way, nor is it representative of any final product
    def example_login(self):
        self.signed_in = True
        self.username = "Example123"
        self.account_age = "10 months"  # should probably be an int in the future, but str for example purpose
        self.recipes = "chicken and rice\ncorndog\nwaffles\nsloppy joe"  # list of keys to recipes in the DB
        self.tools = "whisk\ncutting board\nblender\ngrill"  # list of strings
        self.pantry = "chicken\nrice\nflour\nground beef"  # list of formatted strings (to include amount + unit)
        self.permissions = "View and Search for recipes \nCreate recipes\nExecute recipes"  # list of bools
        self.settings = User.settings_default
        self.settings["Metric"] = True


    # here are the getters and setters for all the specific requests that need to be done at any point

    def __load_from_db(self):
        pass

    def __save_to_db(self):
        pass

    # we may need to implement some kind of deadman switch to send the logout info to the server
    # if we even need to send that to the server
    def logout(self):
        pass

    def login(self):
        pass

