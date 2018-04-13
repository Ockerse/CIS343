from Player import Player
from Home import Home
from random import randint
from Neighborhood import Neighborhood
from Weapon import Weapon
import Monster
import Observe

##########################################
# Aron Ockerse
# March 22, 2018
# Game class to create game logic
##########################################


class Game(Observe.Observer):

    def __init__(self):
        self.player = Player()
        self.neighborhood = Neighborhood()
        self.home = Home()
        self.weapon = Weapon()
        self.totalMonsters = 0
        self.isPlaying = True

    # if player health is 0 or less game over or total monsters is 0
    def isGameOver(self):
        print(self.neighborhood.getHouseList)
        if self.player.getHealth() <= 0:
            return True
        elif self.neighborhood.getHouseList <= 0:
            return True
        else:
            return False

    # prints player actions
    def options(self):
        print("What would you like to do?")
        print("[Attack] [Items] [Run]")

    def playerTurn(self):
        home = self.neighborhood.getCurrentHouse()
        playerInventory = self.player.getInventory()
        monsterList = home.getList()

        weapon = input("Enter a valid weapon (Hershey Kiss, Chocolate Bar, Sour Straw, Nerd Bomb): ")

        for monster in monsterList:
            for weapon in playerInventory:
                self.player.isAttacking(monster, weapon)
                print("You dealt %u damage to a %s" % (self.player.getAttack(), monster.getName()))
                if monster.getHealth() <= 0:
                    monsterList.remove[monster]
                    print("You defeated a %s" % (monster.getName()))

    def playerAttack(self, monsterName, weaponName):
        self.player.isAttacking(monsterName, weaponName)

    def monsterAttack(self):
        total = 0
        home = self.neighborhood.getCurrentHouse()

        monsterList = home.getList()

        for monster in monsterList:
            total += monster.getAttack()

        Player.setHealth((Player.getHealth - total))

    # returns player's health
    def getPlayerHealth(self):
        return self.player.getHealth()

    def printInventory(self):
        for item in self.player.getInventory():
            print(item)

    # returns number of monsters in current house
    def getHouseInfo(self):
        return self.home.getNumMonsters()

    # returns total monter health in current house
    def getHouseHealth(self):
        return self.home.getTotalMonsterHealth()

    # returns player
    def getPlayer(self):
        return self.player

    # returns current house
    def getCurrentHome(self):
        return self.currentHome

    # returns total number of monsters in hosue
    def getTotalMonsters(self):
        house = self.neighborhood.getHouseList()
        for monsters in house:
            totalMonsters += 1
        return self.totalMonsters

    # set number of monters in hosue
    def setTotalMonsters(self, newTotal):
        self.totalMonsters = newTotal
