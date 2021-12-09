# this can be removed if/when the actual list is generated and stored in the db/ somewhere else
from dataManagement import database

database = database.Database()


# Old hardcoded stuff
# Proteins = ["chicken", "pork", "beef", "beans"]
# Dairy = ["milk (2%)", "milk (whole)", "heavy cream", "cheese"]
# Spices = ["salt", "pepper", "cumin", "allspice"]
# Fruit = ["apple", "banana", "orange"]
# Vegetable = ["carrot", "celery", "cucumber", "lettuce"]
# Other = ["water", "flour", "yeast", "honey"]
# sweeteners?

Proteins = database.getIngredients("Protein")
Dairy = database.getIngredients("Dairy")
Spices = database.getIngredients("Spice")
Fruit = database.getIngredients("Fruit")
Vegetable = database.getIngredients("Vegetable")
Other = database.getIngredients("Other")


ingredients = Proteins + Dairy + Spices + Fruit + Vegetable + Other

#dictionary of terms lists
all = {"Proteins":Proteins,
       "Dairy": Dairy,
       "Spices": Spices,
       "Fruit": Fruit,
       "Vegetable": Vegetable,
       "Other": Other
       }
# Old hardcoded tools
# Mixer = ["stand mixer", "blender"]
# Utensil = ["fork", "knife", "spoon", "ladle"]
# Dish = ["bowl", "plate", "pot", "pan"]
# Other = ["cutting board", "hot mitt"]

Mixer = database.getTools("Mixer")
Utensil = database.getTools("Utensil")
Dish = database.getTools("Dish")
Other = database.getTools("Other")

all_tools = {"Mixer": Mixer, "Utensil": Utensil, "Dish":Dish, "Other":Other}
tools = Mixer + Utensil + Dish + Other


#           unit name       metric * value in chart = imperial
# value in chart = 1 means that the unit is in whole objects, not a measuring system
# conversion = {
#        "gram(s)": 0.002204623,      # lbs
#        "ml(s)": 0.03519508,  # ounce oz
#        "egg(s)":1,
#        "lemon(s)":1,
#        "tomato(es)":1,
#        "pepper(s)":1,
#        "crown(s)":1,
#        "carrot(s)":1,
#        "clove(s)":1,
#        "onion(s)":1,
#        "leaf(s)":1
# }





units = "fill this in later"