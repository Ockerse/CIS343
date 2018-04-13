from Home import Home
from random import randint
import Monster
import Observe

##########################################
# Aron Ockerse
# March 22, 2018
# Neighborhood class to set neighborhood
##########################################


class Neighborhood(Observe.Observable):

    def __init__(self):
        self.housesList = []
        self.currentHouse = 0

    # addHouse is used to store a certain amount of houses dependeding on difficulty
    def addHouse(self, difficulty):

        # adds 3 houses if easy
        if ('easy' in difficulty or 'Easy' in difficulty):
            for x in range(3):
                self.housesList.append(Home())

        # adds 5 houses if meduim
        if ('meduim' in difficulty or 'Meduim' in difficulty):
            for x in range(5):
                self.housesList.append(Home())

        # adds 10 houses if hard
        if ('hard' in difficulty or 'Hard' in difficulty):
            for x in range(10):
                self.housesList.append(Home())
        print(self.housesList)

    # moves on to next house in list
    def incCurrentHouse(self):
        self.currentHouse = self.getCurrentHouse + 1

    # returns list of houses
    def getHouseList(self):
        return self.housesList

    # returns current hosue player is on
    def getCurrentHouse(self):
        return self.housesList[self.currentHouse]
