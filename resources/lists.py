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

all_tools = {"Mixer":Mixer, "Utensil":Utensil, "Dish":Dish, "Other":Other}
tools = Mixer + Utensil + Dish + Other




units = "fill this in later"