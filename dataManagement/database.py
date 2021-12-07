import mysql.connector

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
        print(self.db)

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


