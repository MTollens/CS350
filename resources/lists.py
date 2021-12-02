# this can be removed if/when the actual list is generated and stored in the db/ somewhere else

Proteins = ["chicken", "pork", "beef", "beans"]
Dairy = ["milk (2%)", "milk (whole)", "heavy cream", "cheese"]
Spices = ["salt", "pepper", "cumin", "allspice"]
Fruit = ["apple", "banana", "orange"]
Vegetable = ["carrot", "celery", "cucumber", "lettuce"]
Other = ["water", "flour", "yeast", "honey"]
# sweeteners?

ingredients = Proteins + Dairy + Spices + Fruit + Vegetable + Other

#dictionary of terms lists
all = {"Proteins":Proteins,
       "Dairy": Dairy,
       "Spices": Spices,
       "Fruit": Fruit,
       "Vegetable": Vegetable,
       "Other": Other
       }

Mixer = ["stand mixer", "blender"]
Utensil = ["fork", "knife", "spoon", "ladle"]
Dish = ["bowl", "plate", "pot", "pan"]
Other = ["cutting board", "hot mitt"]

all_tools = {"Mixer":Mixer, "Utensil":Utensil, "Dish":Dish, "Other":Other}
tools = Mixer + Utensil + Dish + Other




units = "fill this in later"