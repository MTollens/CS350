import json
from dataManagement import common_utils

class Ingredients:
    def __init__(self):
        # array of x height, and 3 depth:
        """
               0          1          2
        x     name      amount      unit
        0     chicken     5         pounds
        1     pepper      2         tbsp
        2     salt        3         pinch
        3     water       2         cups
        etc....
        """
        # instance using :    object = ingredients.Ingredients().example() # to get this exact setup for testing
        self.items = []

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
        self.items = [
            ["chicken", 5, "lbs"],
            ["pepper", 2, "tbsp"],
            ["salt", 3, "pinch"],
            ["water", 2, "cups"]
        ]
        return self

    # will return a string of the ingredients array, may not need to be private, we shall see
    def tostring(self):
        return self.items.__repr__()

    # appends an item to the array, will check the format and alert if problem
    # TODO implement rollback of ingredients list if added ingredient is invalid
    # may not be required if we dont allow foreign items
    def add_item(self, item):
        assert isinstance(item, list), "item must be a list"
        assert len(item) == 3, "must be a three item list"
        # check if the unit is metric or imperial
        if item[2] in ["lb(s)", "oz(s)"]:
            item[2], item[1] = self.__convert_units_to_metric(item[2], item[1])
        self.items.append(item)
        return self.validate()

    # removes the ingredient from the list at the given indice
    def remove_item(self, indice):
        # not tested! WARNING
        del self.items[indice]
        return True

    # implementing a python builtin, not sure if needed at all
    def __repr__(self):
        return str(json.dumps(self.items))

    # takes a string, and returns the new object
    def from_string(self, string):
        self.__unit = "metric"
        self.__origin = "string"
        return self
        pass

    # returns a nicely formatted string for display where applicable
    def pretty(self):
        temp = ""
        for x in self.items:
            temp = temp + "- {}, {} {} \n".format(x[0], x[1], x[2])
        return temp

    def pretty_imperial(self):
        temp = ""
        for x in self.items:
            unit, value = common_utils.convert_units_to_imperial(x[2], x[1])
            temp = temp + "- {}, {} {} \n".format(x[0], value, unit)
        return temp

    # returns the origin, a string
    def get_origin(self):
        return self.__origin

    # changes the unit flag, does not actually convert the listed units or values,
    # units are always generated dynamically
    @DeprecationWarning
    def convert_unit(self):
        if self.__unit == "metric":
            self.__unit = "imperial"
        else:
            self.__unit = "metric"

    # checks contents of the ingredients array against allowed values, returns true on valid, false on invalid
    #shouldnt end up needing this, since the inputs are prevalidated
    def validate(self):
        from resources import lists
        # return the index of the variable that was wrong if false
        for x in range(0, len(self.items)):
            if self.items[0][x] not in lists.ingredients:
                return x
        return True

    # makes it so that the <class Ingredients()> is able to be called as such:
    # Ingredients_instance[0] # returns the first instance of the list
    # also:
    # Ingredients_instance[0][0] # returns the first ingredient string in the case of example "chicken"
    def __getitem__(self, item):
        return self.items[item]

    @DeprecationWarning
    def metric(self):
        return self.__unit == "metric"


    # DO NOT EXPORT THIS FUNCTION TO ANY OTHER PAGES
    # YOU SHOULD NEVER NEED THIS
    def __convert_units_to_metric(self, unit, value):
        # warnings.warn("WARNING: you should not use this method if you can help it, you should just recall the original value")
        gram_to_lb = 0.002204623
        ml_to_oz = 0.03519508
        if unit == "oz(s)":
            return "ml(s)", str(round(float(value)/ml_to_oz, 3))
        if unit == "lb(s)":
            return "gram(s)", str(round(float(value)/gram_to_lb, 3))
        else:
            # unit is measured in whole units, so there is no change
            return unit, value