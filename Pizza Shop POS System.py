#Mega Cool POS Pizza Program
#Developer: Brandon Duong
#Date Created: 11/26/2017
#Version 1.0
#Purpose: POS System for a Pizza Place


sizeDict = {"1": "Small", "2": "Medium", "3": "Large", "4": "X-tra Large"}
toppingDict = {"1": "Cheese", "2": "Pepperoni", "3": "Mushrooms", "4": "Pineapple", "5": "Bacon", "6": "No More!!!"}
drinksDict = {"1": "Soda Can", "2": "Soda 2L Bottle", "3": "Water Bottle", "4": "Vitamin Water"}

class Pizza: #self.size, self.toppings
    def __init__(self):
        self.pizzaSize()
        self.pizzaToppings()
        self.pizzaCost()
        #print (self.size, self.toppings, self.cost) #test
        
    def pizzaSize(self): #Select size
        success = False
        while success == False:
            print ("""
What size of Pizza?
1 - Small
2 - Medium
3 - Large
4 - X-tra Large
""")
            userInput = str(input("Input num: "))
            if userInput in [str(x) for x in range(1, 5)]:
                self.size = sizeDict[userInput]
                success = True
            else:
                print ("Invalid Input")

    def pizzaToppings(self): #Select toppings
        toppings = []
        finished = False
        while finished == False:
            print ("""
What toppings on the pizza?
1 - Cheese
2 - Pepperoni
3 - Mushrooms
4 - Pineapple
5 - Bacon
6 - No More!!!
""")
            userInput = str(input("Input num: "))
            if userInput in [str(x) for x in range(1, 6)]:
                if toppingDict[userInput] not in toppings:
                    toppings.append(toppingDict[userInput])
                print (toppings)
            elif userInput == "6":
                finished = True
            else:
                print ("Invalid Input")
        self.toppings = toppings

    def pizzaCost(self): #Calculate cost of pizza
        sizeCostDict = {"Small": 5, "Medium": 6, "Large": 7, "X-tra Large": 8}
        topCostDict = {"Cheese": 0.5, "Pepperoni": 0.5, "Mushrooms": 1, "Pineapple": 1, "Bacon": 1}
        self.cost = 0
        self.cost += sizeCostDict[self.size]
        for i in self.toppings:
            self.cost += topCostDict[i]

#p = Pizza() #test

#############################################################
class Fries: #self.size
    def __init__(self):
        self.frySize()
        self.fryCost()
        #print(self.frysize, self.fryCost) #test

    def frySize(self): #Select size
        success = False
        while success == False:
            print ("""
What size of Box of Fries?
1 - Small
2 - Medium
3 - Large
""")
            userInput = str(input("Input num: "))
            if userInput in [str(x) for x in range(1, 4)]:
                self.size = sizeDict[userInput]
                success = True
            else:
                print ("Invalid Input")

    def fryCost(self): #Calculate cost of fries
        sizeCostDict = {"Small": 3, "Medium": 4, "Large": 5}
        self.cost = sizeCostDict[self.size]
#############################################################
class Drinks: #self.type
    def __init__(self):
        self.drinkType()
        self.drinkCost()
        #print(self.type) #test

    def drinkType(self): #Select type
        success = False
        while success == False:
            print ("""
What type of drink?
1 - Soda Can
2 - Soda 2L Bottle
3 - Water Bottle
4 - Vitamin Water
""")
            userInput = str(input("Input num: "))
            if userInput in [str(x) for x in range(1, 5)]:
                self.type = drinksDict[userInput]
                success = True
            else:
                print ("Invalid Input")

    def drinkCost(self): #Calculate cost
        drinkCostDict = {"Soda Can": 1, "Soda 2L Bottle": 3.50, "Water Bottle": 0.75, "Vitamin Water": 1.75}
        self.cost = drinkCostDict[self.type]
    
#############################################################
class User: #self.__username
    def __init__(self, username): #Assign username
        self.__username = username

    def getUsername(self): #Return username
        return self.__username

#u = User() #test
#############################################################
import time
from timeit import default_timer as timer

userDict = {} #Username and Password Dictionary for Logging in/Registering
loggedIn = False

while True: #Program always runs
    startTimer = timer() #Starting time
    while loggedIn == False: #Not logged in
        print ("Welcome to the Pizza Program!")
        choice = str(input("Would you like to login, or register? (L, R) "))
        if choice == "L": #Login
            print ("Login")
            loginUser = str(input("Username: "))
            loginPass = str(input("Password: "))
            
            if loginUser not in userDict: #Catch invalid username
                print ("Stop trying to hack into people's accounts! >:(")
                
            elif userDict[loginUser] == loginPass: #Login
                loggedIn = True
                currentUser = User(loginUser)
                
                logTime = timer() #Login Time
                log = open("log.txt", "a")
                log.write(str(currentUser.getUsername()) + " Logged in at: " + str(logTime) + "\n")
                log.close()
                
                print ("You logged in!")

            else: #Catch wrong pass
                print ("Stop trying to hack into people's accounts! >:(")

        if choice == "R": #Register
            success = False
            while success == False:
                username = str(input("Username: "))
                if username not in userDict:
                    success = True
                else:
                    print ("Username taken!")
            password = str(input("Password: "))
            userDict[username] = password

    while loggedIn == True: #Logged in
        print ("""What would you like to do?
1 - Take Order
2 - Logout
3 - Sales History + Login and Logout History
""")
        choice = str(input("Input num: "))
        if choice == "1": #Take Orders
            fullOrder = []
            fullCost = 0
            numPizza = int(input("Number of Pizzas: "))
            numFries = int(input("Number of Boxes of Fries: "))
            numDrinks = int(input("Number of Drinks: "))
            while numPizza > 0: #Ordering Pizzas
                currentPizza = Pizza()
                fullOrder.append([currentPizza.size + " Pizza with: " +str(currentPizza.toppings)])
                fullCost += currentPizza.cost
                numPizza -= 1

            while numFries > 0: #Ordering Fries
                currentFries = Fries()
                fullOrder.append([currentFries.size + " Fries"])
                fullCost += currentFries.cost
                numFries -= 1

            while numDrinks > 0: #Ordering Drinks
                currentDrink = Drinks()
                fullOrder.append([currentDrink.type])
                fullCost += currentDrink.cost
                numDrinks -= 1

            success = False
            while success == False: #Cancelling Option
                cancel = str(input("Would you like to cancel? (Y, N) "))
                if cancel == "Y":
                    choice = "0"
                    success = True
                
                elif cancel == "N": #Receipt Making
                    success = True
                    receipt = open("receipt.txt", "w")
                    receipt.write("Full Order: \n")
                    print (fullOrder)
                    for i in range (0, len(fullOrder)):
                        receipt.write(str(fullOrder[i]) + "\n")
                        
                    receipt.write("Total Cost: " + str(fullCost) + "\n")
                    receipt.close()
                    
                else: #Catching Invalid Input
                    print ("Invalid Input")

            receipt = open("receipt.txt", "r") #Read and print receipt
            data = receipt.read()
            print ("")
            print (data)
            
            salesHistory = open("salesHistory.txt", "a") #Add current sale to sales history
            salesHistory.write("User: " + currentUser.getUsername() + "\n")
            salesHistory.write(data)
            salesHistory.write("\n")

            salesHistory.close()
            receipt.close()

        if choice == "2": #Logout
            logTime = timer() #Logout Time
            log = open("log.txt", "a")
            log.write(str(currentUser.getUsername()) + " Logged out at: " + str(logTime) + "\n")
            log.close()
            loggedIn = False

        elif choice == "3": #Sales History + Login and Logout History
            print ("Sales History: ") #Sales History
            salesHistory = open("salesHistory.txt", "r")
            history = salesHistory.read()
            print (history)

            print ("Login and Logout History: \n") #Login and Out History
            log = open("log.txt", "r")
            logHistory = log.read()
            print (logHistory)
            choice = "0"



