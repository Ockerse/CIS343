import Monster
import Observe
from random import randint


class Home(Observe.Observer, Observe.Observable):

    def __init__(self):
        Observe.Observable.__init__(self)
        self.totalMonsters = randint(0, 10)
        self.monsterList = []

        for x in range(self.totalMonsters):
            monsterRandomizer = randint(0, 4)

            if (monsterRandomizer == 0):
                self.monsterList.append(Monster.Zombie(self))

            if (monsterRandomizer == 1):
                self.monsterList.append(Monster.Vampire(self))

            if (monsterRandomizer == 2):
                self.monsterList.append(Monster.Ghoul(self))

            if (monsterRandomizer == 3):
                self.monsterList.append(Monster.Werewolf(self))

            if (monsterRandomizer == 4):
                self.monsterList.append(Monster.Person(self))

            super().__init__()

    def getList(self):
        return self.monsterList

    def setList(self, insertList):
        self.monsterList = insertList

    def getNumMonsters(self):
        total = 0
        for monster in self.getList():
            # if(monster.getName() != "Person"):
            total += 1
        return total

    def getTotalMonsterHealth(self):
        total = 0
        for monster in self.getList():
            if(monster.getName() != "Person"):
                total += monster.getHealth()
        return total
