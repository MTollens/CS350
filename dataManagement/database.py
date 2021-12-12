import mysql.connector
import json
from dataManagement import recipe
from dataManagement import ingredients

class Database():
    # If an error occurs here bc of bad password make sure the following are true
    # A file simply called "password" exists in the CS350 directory (same directory as main.py)
    # There is only 1 line in the file of which contains your mySQL root password in plain text
    # You also need to have database "recipebuddy" created and updated with update_database.bat
    def __init__(self):
        pfile = open("password", "r")
        password = pfile.read()
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password
        )
        pfile.close()

        # dbcursor is where mySQL commands are executed and results are returned
        self.dbcursor = self.db.cursor()

        # Checks to make sure recipebuddy exists
        self.dbcursor.execute("SHOW DATABASES")
        dbFound = False
        for x in self.dbcursor:
            if x[0] == "recipebuddy":
                dbFound = True

        if not dbFound:
            print("ERROR: recipebuddy DB not found!")
            quit()
        else:
            # Database is found and can safely use it
            print("recipebuddy DB found.")
            self.dbcursor.execute("USE recipebuddy")

    def verifyLogin(self, username, password):
        query = "SELECT username, password FROM account WHERE username = %s AND password = %s"
        inputs = (username, password, )
        self.dbcursor.execute(query, inputs)

        result = self.dbcursor.fetchone()
        if result:
            print("Logged in as " + username)
            return username, password
        else:
            print("Login failed!")
            pass

    def createAccount(self, username, password):
        query = "INSERT INTO account VALUES (%s, %s, 0, 'Metric')"
        inputs = (username, password, )

        self.dbcursor.execute(query, inputs)

        self.db.commit()
        return self.dbcursor.rowcount

    def getUsernames(self):
        query = "SELECT username FROM account"

        self.dbcursor.execute(query)

        result = self.dbcursor.fetchall()

        if result:
            cleanList = []
            for x in result:
                cleanList.append(x[0])
            return cleanList
        else:
            return




    def getAccountInfo(self, username):
        query = "SELECT private, measurement_system FROM account WHERE username = %s"
        input = (username, )
        self.dbcursor.execute(query, input)
        result = self.dbcursor.fetchone()

        if result:
            return result
        else:
            print("Error fetching user account information")
            pass

    def switchPrivacy(self, username, private):
        if private:
            query = "UPDATE account SET private = 1 where username = %s"
        else:
            query = "UPDATE account SET private = 0 where username = %s"
        input = (username, )
        self.dbcursor.execute(query, input)
        self.db.commit()
        print(self.dbcursor.rowcount, "record(s) affected")

    def switchUnits(self, username, metric):
        if metric:
            query = "UPDATE account SET measurement_system = 'Imperial' where username = %s"
        else:
            query = "UPDATE account SET measurement_system = 'Metric' where username = %s"
        input = (username, )
        self.dbcursor.execute(query, input)
        self.db.commit()
        print(self.dbcursor.rowcount, "record(s) affected")

    # Ingredient Fetching
    def getIngredients(self, category):
        if category != "Other":
            query = "SELECT name FROM ingredient WHERE category = %s"
            input = (category,)
            self.dbcursor.execute(query, input)
        else:
            query = "SELECT name FROM ingredient WHERE category IS NULL"
            self.dbcursor.execute(query)

        result = self.dbcursor.fetchall()

        if result:
            cleanList = []
            for x in result:
                cleanList.append(x[0])

            return cleanList
        else:
            return

    def getIngredientUnit(self, ingredient):
        query = "SELECT unit FROM ingredient WHERE name = %s"
        input = (ingredient, )

        self.dbcursor.execute(query, input)

        result = self.dbcursor.fetchone()

        if result:
            return result[0]
        else:
            return

    def saveRecipe(self, recipe):
        query = "INSERT INTO recipe VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # TODO All parsing here needs to be "deparsed"
        # Parse ingredients to be put into database properly
        ingredientList = json.dumps(recipe.ingredients.items)

        # Parse tools
        toolList = json.dumps(recipe.tools)

        # Parse tags
        tagList = json.dumps(recipe.tags)

        instructionList = json.dumps(recipe.instructions)

        input = (recipe.title, recipe.owner, ingredientList, toolList, instructionList, recipe.servings, recipe.prep_time, tagList, recipe.times_exec, recipe.image, )
        self.dbcursor.execute(query, input)

        self.db.commit()

        return self.dbcursor.rowcount


    def deleteRecipe(self, recipe):
        query = "DELETE FROM recipe WHERE name = %s"

        input = (recipe.title, )
        self.dbcursor.execute(query, input)

        self.db.commit()

        return self.dbcursor.rowcount

    def loadRecipeByOwner(self, owner):
        recipeList = []

        # Individual queries for each param (almost certainly a better way to do this but meh)
        nameQuery = "SELECT name FROM recipe WHERE creator = %s"
        creatorQuery = "SELECT creator FROM recipe WHERE creator = %s"
        ingredientsQuery = "SELECT ingredients FROM recipe WHERE creator = %s"
        appliancesQuery = "SELECT appliances FROM recipe WHERE creator = %s"
        instructionsQuery = "SELECT instructions FROM recipe WHERE creator = %s"
        serving_sizeQuery = "SELECT serving_size FROM recipe WHERE creator = %s"
        prep_timeQuery = "SELECT prep_time FROM recipe WHERE creator = %s"
        tagsQuery = "SELECT tags FROM recipe WHERE creator = %s"
        times_executedQuery = "SELECT times_executed FROM recipe WHERE creator = %s"
        imageQuery = "SELECT image FROM recipe WHERE creator = %s"

        input = (owner, )

        self.dbcursor.execute(nameQuery, input)
        nameRows = self.dbcursor.fetchall()

        if nameRows:

            self.dbcursor.execute(creatorQuery, input)
            creatorRows = self.dbcursor.fetchall()

            self.dbcursor.execute(ingredientsQuery, input)
            ingredientsRows = self.dbcursor.fetchall()

            self.dbcursor.execute(appliancesQuery, input)
            appliancesRows = self.dbcursor.fetchall()

            self.dbcursor.execute(instructionsQuery, input)
            instructionsRows = self.dbcursor.fetchall()

            self.dbcursor.execute(serving_sizeQuery, input)
            serving_sizeRows = self.dbcursor.fetchall()

            self.dbcursor.execute(prep_timeQuery, input)
            prep_timeRows = self.dbcursor.fetchall()

            self.dbcursor.execute(tagsQuery, input)
            tagsRows = self.dbcursor.fetchall()

            self.dbcursor.execute(times_executedQuery, input)
            times_executedRows = self.dbcursor.fetchall()

            self.dbcursor.execute(imageQuery, input)
            imageRows = self.dbcursor.fetchall()

            for x in range(len(nameRows)):
                tempRecipe = recipe.Recipe(owner=owner)
                tempRecipe.title = nameRows[x][0]
                tempIngredients = ingredients.Ingredients()
                tempIngredients.items = json.loads(ingredientsRows[x][0])
                tempRecipe.ingredients = tempIngredients
                tempRecipe.tools = json.loads(appliancesRows[x][0])
                tempRecipe.instructions = json.loads(instructionsRows[x][0])
                tempRecipe.servings = serving_sizeRows[x][0]
                tempRecipe.prep_time = prep_timeRows[x][0]
                tempRecipe.tags = json.loads(tagsRows[x][0])
                tempRecipe.times_exec = times_executedRows[x][0]
                tempRecipe.image = imageRows[x][0]
                recipeList.append(tempRecipe)


            return recipeList
        else:
            return []

    def loadRecipeByFeatured(self):
        recipeList = []

        # Individual queries for each param (almost certainly a better way to do this but meh)
        nameQuery = "SELECT name FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        creatorQuery = "SELECT creator FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        ingredientsQuery = "SELECT ingredients FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        appliancesQuery = "SELECT appliances FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        instructionsQuery = "SELECT instructions FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        serving_sizeQuery = "SELECT serving_size FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        prep_timeQuery = "SELECT prep_time FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        tagsQuery = "SELECT tags FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        times_executedQuery = "SELECT times_executed FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"
        imageQuery = "SELECT image FROM recipe GROUP BY name ORDER BY COUNT(times_executed)"


        self.dbcursor.execute(nameQuery)
        nameRows = self.dbcursor.fetchall()

        if nameRows:

            self.dbcursor.execute(creatorQuery)
            creatorRows = self.dbcursor.fetchall()

            self.dbcursor.execute(ingredientsQuery)
            ingredientsRows = self.dbcursor.fetchall()

            self.dbcursor.execute(appliancesQuery)
            appliancesRows = self.dbcursor.fetchall()

            self.dbcursor.execute(instructionsQuery)
            instructionsRows = self.dbcursor.fetchall()

            self.dbcursor.execute(serving_sizeQuery)
            serving_sizeRows = self.dbcursor.fetchall()

            self.dbcursor.execute(prep_timeQuery)
            prep_timeRows = self.dbcursor.fetchall()

            self.dbcursor.execute(tagsQuery)
            tagsRows = self.dbcursor.fetchall()

            self.dbcursor.execute(times_executedQuery)
            times_executedRows = self.dbcursor.fetchall()

            self.dbcursor.execute(imageQuery)
            imageRows = self.dbcursor.fetchall()

            for x in range(len(nameRows)):
                tempRecipe = recipe.Recipe(owner=creatorRows[x][0])
                tempRecipe.title = nameRows[x][0]
                tempIngredients = ingredients.Ingredients()
                tempIngredients.items = json.loads(ingredientsRows[x][0])
                tempRecipe.ingredients = tempIngredients
                tempRecipe.tools = json.loads(appliancesRows[x][0])
                tempRecipe.instructions = json.loads(instructionsRows[x][0])
                tempRecipe.servings = serving_sizeRows[x][0]
                tempRecipe.prep_time = prep_timeRows[x][0]
                tempRecipe.tags = json.loads(tagsRows[x][0])
                tempRecipe.times_exec = times_executedRows[x][0]
                tempRecipe.image = imageRows[x][0]
                recipeList.append(tempRecipe)

            return recipeList
        else:
            return []

    # Tool Fetching
    def getTools(self, category):
        if category != "Other":
            query = "SELECT name FROM appliance WHERE category = %s"
            input = (category,)
            self.dbcursor.execute(query, input)
        else:
            query = "SELECT name FROM appliance WHERE category IS NULL"
            self.dbcursor.execute(query)

        result = self.dbcursor.fetchall()

        if result:
            cleanList = []
            for x in result:
                cleanList.append(x[0])
            return cleanList
        else:
            return


