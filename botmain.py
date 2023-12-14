# INF601 - Advanced Programming in Python
# Stephen Gabel
# Final Project


# This project sends drop data up to a website to display the statistics of that data.


import pyautogui
import pyautogui as pag
import time
import os
import pandas as pd
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
"""def cardReader():

    #buffer to allow swap to game
    time.sleep(5)

    #Create card class. This will allow the stats and schools of each card to follow this formula
    class attackcard():
        def __init__(self, name, school, mindamage, maxdamage, castchance):
            self.name = name
            self.school = school
            self.mindamage = mindamage
            self.maxdamage = maxdamage
            self.castchance = castchance

    #Different cards and their names.

    bloodbat = attackcard('bloodbat', 'myth',70, 110,0.8)
    itembloodbat = attackcard('itembloodbat','myth',60,100,0.8)
    itemdarksprite = attackcard('itemdarksprite','death',55,95,0.85)
    itemfirecat = attackcard('itemfirecat','fire',70,110,0.75)
    itemfrostbeetle = attackcard('itemfrostbeetle','ice',55,95,0.8)
    itemimp = attackcard('itemimp','life', 55,95,0.9)
    itemscarab = attackcard('itemscarab','balance',55,95,0.85)
    itemthundersnake = attackcard('itemthundersnake','storm',95,135,0.7)

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

    print(cardlist.bloodbat.__dict__['name'])


cardReader()"""
#def pathFinder():

    #Keep track of quest arrow direction and move based upon it.

    #Keep track of whether player is in battle or not.

    #Keep track of what the quest wants

    #If an interaction occurs, activate the interactionAutomator.


#def interactionAutomator():

    #Navigate interactions based upon what they are.


def inventoryTracker():
    drops = []
    equipmentlist = {"equipmentdrops": drops}

    print("How many battles have occurred?")

    while True:
        battlecount = input()

        if battlecount.isdecimal():
            break

        else:
            print("That is not a number.")

    print("what gear did you aquire? List duplicates as well. Do not use any punctuation. Once finished, type finish.")
    while True:
        listinput = input()
        if listinput == 'finish':
            break

        elif listinput.isdecimal():
            print("Please refrain from using numbers.")

        else:
            drops.append(listinput)

    equipmentframe = pd.DataFrame.from_dict(equipmentlist, orient="columns")
    organizedequipmentframe = equipmentframe.groupby('equipmentdrops')['equipmentdrops'].count().sort_values(ascending=[1]).tail()
    print(organizedequipmentframe)



inventoryTracker()




#def dropTracker():

    #Use the inventoryTracker to make comparisons from the inventory.

    #Store the data inside a pandas dataframe, which will be passed onto the API.

#def botWrapper():

    #bundles the bot functions into one process.



