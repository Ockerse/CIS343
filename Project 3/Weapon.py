from random import randint
from abc import ABCMeta, abstractmethod


##########################################
# Aron Ockerse
# March 22, 2018
# Weapon class to manupualte weapon data
##########################################

class Weapon(object):
    __metaclass__ = ABCMeta

    name = ""
    modifier = 0
    uses = 0
    MAX_USES = 0

    # checks item uses left
    def usesLeft(self):
        if (self.uses < self.MAX_USES):
            return True
        else:
            return False

    # returns item name
    def getWeaponName(self):
        return self.name

    # gets item modifier
    def getModifier(self):
        return self.modifier

    # returns item uses
    def getUses(self):
        return self.uses

    # returns item maximun uses
    def getMax_Uses(self):
        return self.MAX_USES


# HersheyKisses class
class HersheyKisses(Weapon):

    def __init__(self):
        self.name = "Hershey Kiss"
        self.modifier = 1
        self.MAX_USES = float("inf")

# SourStraws class


class SourStraws(Weapon):

    def __init__(self):
        self.name = "Sour Straw"
        self.modifier = randint(100, 175) / 100
        self.MAX_USES = 2

# ChocolateBars class


class ChocolateBars(Weapon):

    def __init__(self):
        self.name = "Chocolate Bar"
        self.modifier = randint(200, 240) / 100
        self.MAX_USES = 4

# NerdBombs class


class NerdBombs(Weapon):

    def __init__(self):
        self.name = "Nerd Bomb"
        self.modifier = randint(350, 500) / 100
        self.MAX_USES = 1
