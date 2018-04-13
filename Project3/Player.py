import Weapon
import Monster
import Observe
from random import randint

##########################################
# Aron Ockerse
# March 22, 2018
# Player class to manupualte player action
##########################################


class Player(Observe.Observable):

    # sets health, attack and inventory to empty
    health = 0
    attack = 0
    inventory = []

    def __init__(self):
        Observe.Observable.__init__(self)

        # sets health to random number between 100-125
        self.health = randint(100, 125)

        # sets attack to random number between 100-125
        self.attack = randint(10, 20)

        # fills list with 10 random weapons
        for x in range(10):
            randomizer = randint(1, 4)

            if(randomizer == 1):
                self.inventory.append(Weapon.HersheyKisses)

            if(randomizer == 2):
                self.inventory.append(Weapon.SourStraws)

            if(randomizer == 4):
                self.inventory.append(Weapon.ChocolateBars)

            if(randomizer == 2):
                self.inventory.append(Weapon.NerdBombs)

    # if player's helth is less then or equal to zero game is over
    def isDead(self):
        if(self.health <= 0):
            return True
        else:
            return False

    # returns player's inventory
    def getInventory(self):
        return self.inventory

    # sets player's inventory
    def setInventory(self, insertInventory):
        self.inventory = insertInventory

    # gets player's health
    def getHealth(self):
        return self.health

    # set player's health
    def setHealth(self, insertHealth):
        self.health = insertHealth

    # get player's attack
    def getAttack(self):
        return self.attack

    # set player's attack
    def setAttack(self, insertAttack):
        self.attack = insertAttack

    # removes items if it has no more uses
    def updateInventory(self, weapon):
        if weapon.getUses is False:
            self.inventory.remove(weapon)

    # takes in a monster and weapon and calculates proper damage
    def isAttacking(self, playerMonster, playerWeapon):
        if playerWeapon.getWeaponName() in "Hershey Kiss":
            playerMonster.setHealth(playerMonster.getHealth -
                                    self.attack * playerWeapon.getModifier)
            Monster.update()

        if playerWeapon.getWeaponName() in "Sour Straw":
            if playerMonster.getName() in "Zombie":
                playerMonster.setHealth(playerMonster.getHealth - 2 *
                                        (self.attack * playerWeapon.getModifier))
            Monster.update()
            if playerMonster.getName() in "Werewolf":
                pass
            else:
                playerMonster.setHealth(playerMonster.getHealth -
                                        self.attack * playerWeapon.getModifier)
        Monster.update()

        if playerWeapon.getWeaponName() in "Chocolate Bar":
            if playerMonster.getName() in "Vampire" or playerWeapon.getWeaponName() in "Werewolf":
                pass
            else:
                playerMonster.setHealth(playerMonster.getHealth -
                                        self.attack * playerWeapon.getModifier)
            Monster.update()

        if playerWeapon.getWeaponName() in "Nerd Bomb":
            if playerMonster.getName() in "Ghoul":
                playerMonster.setHealth(playerMonster.getHealth - 5 *
                                        (self.attack * playerWeapon.getModifier))
                Monster.update()
            else:
                playerMonster.setHealth(playerMonster.getHealth -
                                        self.attack * playerWeapon.getModifier)
                Monster.update()
