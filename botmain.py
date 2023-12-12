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

# Look at what cards are in hand and make a list
def cardReader():

    #buffer to allow swap to game
    time.sleep(5)

    #Create card class. This will allow the stats and schools of each card to follow this formula
    class attackcard():
        def __init__(self, school, mindamage, maxdamage, castchance):
            self.school = school
            self.mindamage = mindamage
            self.maxdamage = maxdamage
            self.castchance = castchance

    #Different cards and their names.

    bloodbat = attackcard('myth',70, 110,0.8)
    itembloodbat = attackcard('myth',60,100,0.8)
    itemdarksprite = attackcard('death',55,95,0.85)
    itemfirecat = attackcard('fire',70,110,0.75)
    itemfrostbeetle = attackcard('ice',55,95,0.8)
    itemimp = attackcard('life', 55,95,0.9)
    itemscarab = attackcard('balance',55,95,0.85)
    itemthundersnake = attackcard('storm',95,135,0.7)

    #Create an empty list this list will list the cards in our hand.
    cardlist = []

    #locate cards. If located, store location in variables. If not, display string.
    try:
        pyautogui.locateOnScreen('bloodbat.jpg',confidence=0.75)
        cardlist.append(bloodbat)
    except: print("bloodbat not found")

    try:
        pyautogui.locateOnScreen('itembloodbat.jpg',confidence=0.75)
        cardlist.append(itembloodbat)
    except: print("item bloodbat not found")

    try:
        pyautogui.locateOnScreen('itemdarksprite.jpg',confidence=0.75)
        cardlist.append(itemdarksprite)
    except: print("item dark sprite not found")

    try:
        pyautogui.locateOnScreen('itemfirecat.jpg',confidence=0.75)
        cardlist.append(itemfirecat)
    except: print("item fire cat not found")

    try:
        pyautogui.locateOnScreen('itemfrostbeetle.jpg',confidence=0.75)
        cardlist.append(itemfrostbeetle)
    except: print("item frost beetle not found")

    try:
        pyautogui.locateOnScreen('itemimp.jpg',confidence=0.75)
        cardlist.append(itemimp)
    except: print("item imp not found")

    try:
        pyautogui.locateOnScreen('itemscarab.jpg',confidence=0.75)
        cardlist.append(itemscarab)
    except: print("item scarab not found")

    try:
        pyautogui.locateOnScreen('itemthundersnake.jpg',confidence=0.75)
        cardlist.append(itemthundersnake)
    except: print("item thundersnake not found")

    #Print what's in the hand, as well as the stats.

    for i in cardlist:
        print(i.__dict__)


cardReader()
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



