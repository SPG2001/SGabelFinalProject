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
    #Create an empty list
    cardlist = []

    #buffer to allow swap to game
    time.sleep(5)

    #Look at the hand and see what makes a match. If a match happens, the coordinates are put into a list.
    #If not on screen, the value is zero.
    try:
        bloodbat = pag.locateOnScreen('bloodbat.jpg', confidence=0.8)
        cardlist.append(bloodbat)
    except: bloodbat = 0
    try:
        itembloodbat = pag.locateOnScreen('itembloodbat.jpg', confidence=0.8)
        cardlist.append(itembloodbat)
    except: itembloodbat = 0
    try:
        itemfirecat = pag.locateOnScreen('itemfirecat.jpg', confidence=0.8)
        cardlist.append(itemfirecat)
    except: itemfirecat = 0
    try:
        itemdarksprite = pag.locateOnScreen('itemdarksprite.jpg', confidence=0.8)
        cardlist.append(itemdarksprite)
    except: itemdarksprite = 0
    try:
        itemimp = pag.locateOnScreen('itemimp.jpg', confidence=0.8)
        cardlist.append(itemimp)
    except: itemimp = 0
    try:
        itemstormsnake = pag.locateOnScreen('itemthundersnake.jpg', confidence=0.8)
        cardlist.append(itemstormsnake)
    except: itemstormsnake = 0
    try:
        itemfrostbeetle = pag.locateOnScreen('itemfrostbeetle.jpg', confidence=0.8)
        cardlist.append(itemfrostbeetle)
    except: itemfrostbeetle = 0

    try:
        itemscarab = pag.locateOnScreen('itemscarab.jpg', confidence=0.8)
        cardlist.append(itemscarab)

    except: itemscarab = 0

    try:
        itemheartbeat = pag.locateOnScreen('itemheartbeat.jpg', confidence=0.8)
        cardlist.append(itemheartbeat)
    except: itemheartbeat = 0

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