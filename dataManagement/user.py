from dataManagement import database, recipe
# for timers
import threading
import time
import subprocess

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
        # string
        self.current_search = ""
        # list of strings
        self.current_search_tags = []
        # recipe
        self.open_recipe = recipe.Recipe('user_default')
        # True if the recipe should be in view mode or in execute mode
        self.view_recipe = True

        # TIMERS
        # stored value for timer, not to be edited manually
        self.__timer_value = 0

        # timer control structure
        self.__timer_control = "END"
        # other values: "RUNNING" "STOP" "PAUSE" "RESUME"

        # timer reference, used to update the display for the remaining time
        self.__timer_reference = None

        # timer thread(s)
        self.timers = None

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

    # might not be needed
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


    # here the value should be an integer number of seconds
    # here the timer is a reference to the StaticText that represents the remaining time
    def start_timer(self, value, timer=None):
        assert isinstance(value, int), "Must pass an integer to the start_timer method"
        try:
            self.timers.join()
        except:
            pass
        self.timer_reference = timer
        self.__timer_value = value
        self.__timer_control = "RUNNING"
        self.timers = threading.Thread(target=self.__run_timer)
        self.timers.start()


    # finish the timer and set the value back to 0
    def end_timer(self):
        self.__timer_control = "STOP"

    # finish the timer but dont reset the value, keep it the same
    def pause_timer(self):
        self.__timer_control = "PAUSE"

    # returns true if timer is running, returns false when timer is not running, or does not exist
    def timer_status(self):
        status = False
        try:
            status = self.timers.is_alive()
        except:
            status = False
        if self.__timer_control == "PAUSE":
            status = False
        return status

    def timer_resume(self):
        self.__timer_control = "RESUME"

    # to be used by a thread, not meant to be called
    def __run_timer(self):
        # print("started timer")
        # main loop
        while True:
            # generate the output products
            hours = int(self.__timer_value / 3600)
            minutes = str(int(self.__timer_value / 60))
            if len(minutes) == 1:
                minutes = "0" + minutes
            seconds = str(self.__timer_value % 60)
            if len(seconds) == 1:
                seconds = "0" + seconds
            # if we were given a handler then we can update the display
            if self.timer_reference:
                self.timer_reference.SetLabel("{}:{}:{}".format(hours, minutes, seconds))
            # sleep for one second
            time.sleep(1)
            #decrement the sleep counter
            self.__timer_value -= 1
            # print status for debug
            # print(self.__timer_control)

            #if time has reached zero, or commanded to stop, we full stop
            if (self.__timer_value <= 0) or (self.__timer_control == "STOP"):
                self.__timer_control = "END"
                break
            # if commanded to pause we enter a wait loop that doesnt count the seconds
            elif self.__timer_control == "PAUSE":
                # secondary wait loop for pause
                while True:
                    # timer here is to give the variable lock a chance to change tha value of the control variable
                    time.sleep(1)
                    # print(self.__timer_control)
                    # if the status is changed to resume, we can break the secondary loop
                    if self.__timer_control == "RESUME":
                        self.__timer_control = "RUNNING"
                        break
                    # if the main thread (the main program) is dead, we can stop
                    elif not threading.main_thread().is_alive():
                        return 0

            # if the main thread is dead we can stop
            elif not threading.main_thread().is_alive():
                return 0


        # if we stopped because the time ran out then we can play the alert
        if self.__timer_value <= 0:
            subprocess.run(['python', 'pages/timer_done.py'])
        return 0