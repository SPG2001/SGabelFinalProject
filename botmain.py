import pyautogui
import pyautogui as pag
import time
import os

#def combatReader():
    #Read the enemy health cards and communicate with the SQLite Database for the stats.


#def combatAI():
    #look at the screen and find out how many pips the wizard and enemies have

    #Look at the screen to see how much health everybody has

    #Look at the screen and look at the spells you have

    #Calculate which spell to cast and on who

    #Select target and cast

    #loop from here


def cardReader():
    #Look at what cards are in hand and make a list

    #Create card class. This will allow the stats and schools of each card to follow this formula
    class attackcard():
        def __init__(self, school, mindamage, maxdamage, castchance):
            self.school = school
            self.mindamage = mindamage
            self.maxdamage = maxdamage
            self.castchance = castchance

    bloodbat = attackcard('myth',70, 110,0.8)
    itembloodbat = attackcard('myth',60,100,0.8)
    itemdarksprite = attackcard('death',55,95,0.85)
    itemfirecat = attackcard('fire',70,110,0.75)
    itemfrostbeetle = attackcard('ice',55,95,0.8)
    itemimp = attackcard('life', 55,95,0.9)
    itemscarab = attackcard('balance',55,95,0.85)
    itemthundersnake = attackcard('storm',95,135,0.7)



    #Create an empty list
    cardlist = []

    #buffer to allow swap to game
    time.sleep(5)

    #Look at the hand and see what makes a match. If a match happens, the coordinates are put into a list.
    #If not on screen, the value is zero.
    try:
        class bloodbat():
            bloodbatlocation = pag.locateOnScreen('bloodbat.jpg', confidence=0.8)
            mindamage = 70
            maxdamage = 110
            castchance = 0.8
        cardlist.append(bloodbat.bloodbatlocation)
    except: print("bloodbat not found")
    try:
        class itembloodbat():
            itembloodbatlocation = pag.locateOnScreen('itembloodbat.jpg', confidence=0.8)
            mindamage = 60
            maxdamage = 100
            castchance = 0.8
        cardlist.append(itembloodbat.itembloodbatlocation)
    except: print("item blood bat not found")
    try:
        class itemdarksprite():
            itemdarkspritelocation = pag.locateOnScreen('itemdarksprite.jpg', confidence=0.8)
            mindamage = 55
            maxdamage = 95
            castchance = 0.85
        cardlist.append(itemdarksprite.itemdarkspritelocation)
    except: print("item dark sprite not found")
    try:
        class itemfirecat():
            itemfirecatlocaton = pag.locateOnScreen('itemfirecat.jpg', confidence=0.8)
            mindamage = 70
            maxdamage = 110
            castchance = 0.75
        cardlist.append(itemfirecat.itemfirecatlocation)
    except: print("item firecat not found")
    try:
        class itemfrostbeetle():
            itemfrostbeetlelocation = pag.locateOnScreen('itemfrostbeetle.jpg', confidence=0.8)
            mindamage = 55
            maxdamage = 95
            castchance = 0.8
        cardlist.append(itemfrostbeetle.itemfrostbeetlelocation)
    except: print("item frost beetle found")
    try:
        class itemimp():
            itemimplocation = pag.locateOnScreen('itemimp.jpg', confidence=0.8)
            mindamage = 55
            maxdamage = 95
            castchance = 0.9
        cardlist.append(itemimp.itemimplocation)
    except: print("item imp not found")
    try:
        class itemscarab():
            def __init__(self, location, mindamage, maxdamage, castchance):
                self.location = pag.locateOnScreen('itemscarab.jpg', confidence=0.8)
                self.mindamage = 55
                self.maxdamage = 95
                self.castchance = 0.85
                cardlist.append(itemscarab.__init__(location))
    except: print("item scarab not found")

    try:
        class card():
            def __init__(self, school, mindamage, maxdamage, castchance):
                self.school = school
                self.mindamage = mindamage
                self.maxdamage = maxdamage
                self.castchance = castchance
    except: print("item thunder snake not found")

    try:
        class itemheartbeat():
            itemheartbeatlocation = pag.locateOnScreen('itemheartbeat.jpg', confidence=0.8)
            heal = 245
            castchance = 0.9
        cardlist.append(itemheartbeat.itemheartbeatlocation)
    except: print("item heartbeat not found")

    print(cardlist)


#def pathFinder():

    #Keep track of quest arrow direction and move based upon it.

    #Keep track of whether player is in battle or not.

    #Keep track of what the quest wants

    #If an interaction occurs, activate the interactionAutomator.


#def interactionAutomator():

    #Navigate interactions based upon what they are.


#def inventoryTracker():

    #Keep track of player inventory and be able to make comparisons of equipment.

    #Used for both equipment and drop rate data


#def dropTracker():

    #Use the inventoryTracker to make comparisons from the inventory.

    #Store the data inside a pandas dataframe, which will be passed onto the API.

#def botWrapper():

    #bundles the bot functions into one process.



cardReader()
