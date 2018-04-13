from abc import ABCMeta, abstractmethod
from random import randint
import Observe
import Player


class Monster(Observe.Observable):

    __metaclass__ = ABCMeta
    health = 0
    attack = 0
    name = ""
    canBeAttacked = True

    def getHealth(self):
        return self.health

    def setHealth(self, insertHealth):
        self.health = insertHealth

    def getAttack(self):
        return self.attack

    def setAttack(self, insertAttack):
        self.attack = insertAttack

    def getName(self):
        return self.name

    def setName(self, insertName):
        self.name = insertName

    def getCanGetAttacked(self):
        return self.canBeAttacked

    def setCanGetAttacked(self, canBeAttacked):
        self.canBeAttacked = canBeAttacked

    def monsterAttack(self, player):
        player.setHealth(Player.getHealth - self.attack)


class Zombie(Monster):

    def __init__(self, Monster):
        Observe.Observable.__init__(self)
        self.health = randint(50, 100)
        self.attack = randint(0, 10)
        self.name = "Zombie"

    def isDead(self):
        if(self.health <= 0):
            return True
        else:
            return False


class Vampire(Monster):

    def __init__(self, Monster):
        Observe.Observable.__init__(self)
        self.health = randint(100, 200)
        self.attack = randint(10, 20)
        self.name = "Vampire"

    def isDead(self):
        if(self.health <= 0):
            return True
        else:
            return False


class Ghoul(Monster):

    def __init__(self, Monster):
        Observe.Observable.__init__(self)
        self.health = randint(40, 80)
        self.attack = randint(15, 30)
        self.name = "Ghoul"

    def isDead(self):
        if(self.health <= 0):
            return True
        else:
            return False


class Werewolf(Monster):

    def __init__(self, Monster):
        Observe.Observable.__init__(self)
        self.health = 200
        self.attack = randint(0, 40)
        self.name = "Werewolf"

    def isDead(self):
        if(self.health <= 0):
            return True
        else:
            return False


class Person(Monster):

    def __init__(self, Monster):
        Observe.Observable.__init__(self)
        self.health = 0
        self.attack = -10
        self.name = "Person"
