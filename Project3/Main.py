from Game import Game


if __name__ == '__main__':
    print("Welcome to Zork and Pals")

    game = Game()
    player = game.player
    neighbor = game.neighborhood
    home = game.home

    difficulty = input("Choose Your Difficulty (Easy, Meduim, Hard)")
    neighbor.addHouse(difficulty)
    game.options()

    while ():
        choice = input("Choose your action")

        if (choice in "attack" or choice in "Attack"):
            game.playerAttack()

        if (choice in "items" or choice in "Items"):
            print("Items")
            game.printInventory()

        if (choice in "run" or choice in "Run"):
            exit()
