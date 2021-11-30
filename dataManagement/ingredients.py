class Ingredients:
    def __init__(self):
        # array of x height, and 3 depth:
        """
        x     name      amount      unit
        0     chicken     5         pounds
        1     pepper      2         tbsp
        2     salt        3         pinch
        3     water       2         cups
        etc....
        """ # instance using :    object = ingredients.Ingredients().example() # to get this exact setup for testing
        self.__items = []

        # always defaults to metric
        # this does not denote how the dataManagement is stored in the list, but how the user requests it
        # units are always shown dynamically, to avoid converting between units and gathering +- errors
        self.__unit = "metric"

        # useful for debugging, might not end up being needed
        # does not need to be stored in the DB
        self.__origin = "empty"

    # example with dummy dataManagement
    def example(self):
        self.__unit = "metric"
        self.__origin = "example"
        self.__items = [
            ["chicken", 5, "lbs"],
            ["pepper", 2, "tbsp"],
            ["salt", 3, "pinch"],
            ["water", 2, "cups"]
        ]
        return self

    # will return a string of the ingredients array, may not need to be private, we shall see
    def __tostring(self):
        return self.__items.__repr__()

    # appends an item to the array, will check the format and alert if problem
    # TODO implement rollback of ingredients list if added ingredient is invalid
    # may not be required if we dont allow foreign items
    def add_item(self, item):
        assert isinstance(item, list), "item must be a list"
        assert len(item) == 3, "must be a three item list"
        #insert other validation steps after this
        self.__items.append(item)
        return self.validate()

    # removes the ingredient from the list at the given indice
    def remove_item(self, indice):
        # not tested! WARNING
        del self.__items[indice]
        return True

    # implementing a python builtin, not sure if needed at all
    def __repr__(self):
        return self.__tostring()

    # takes a string, and returns the new object
    def from_string(self, string):
        self.__unit = "metric"
        self.__origin = "string"
        return self
        pass

    # returns the origin, a string
    def get_origin(self):
        return self.__origin

    # changes the unit flag, does not actually convert the listed units or values,
    # units are always generated dynamically
    def convert_unit(self):
        if self.__unit == "metric":
            self.__unit = "imperial"
        else:
            self.__unit = "metric"

    # checks contents of the ingredients array against allowed values, returns true on valid, false on invalid
    def validate(self):
        pass

    # makes it so that the <class Ingredients()> is able to be called as such:
    # Ingredients_instance[0] # returns the first instance of the list
    # also:
    # Ingredients_instance[0][0] # returns the first ingredient string in the case of example "chicken"
    def __getitem__(self, item):
        return self.__items[item]
