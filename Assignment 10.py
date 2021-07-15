# File name: Assignment 10
# Author Name: Ben Sottile
# Date: 11/8/2019
# Description: In this assignment you need to build a game, called the number guessing game.
#
# The game is that the computer "thinks" about a number and we have to guess it. On every guess, the computer will tell us if our guess is in the list or not. The game ends when we find the number. You give the user 3 chances to enter the number.
# Create a simple command line game guessing a whole number.
#
# Let the computer generate 10 numbers randomly between 1-50. capture the numbers in a list.
# Let the user guess a number between 1-50 and do a linear search in the generated list from above.
# Tell the user if their guess was found in the list or tell them it wasn't found and they must retry again for 2 more times. If they didn't guess the correct number then exist the program and tell the user that they lost the game. If they guess the correct number then you can give them an award of 100 dollars.
# To make the game more interesting, you could tell the user with their fist try if they need to guess smaller or larger values.
# Submit your code and the screen shot of your results one for winning and one for loosing.
import time
import random
import webbrowser
class game:
    def __init__(self,player,WinningList,masterList):
        self.player = player
        self.WinningList = WinningList
        self.masterList = masterList
    def getPlayer(self):
        return self.player
    def getWinningList(self):
        return self.WinningList
    def getMasterList(self):
        return self.masterList
    def getInput(self):
        while True:
            try:
                userInput = int(input("What's your Guess?"))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                if (searchList(self.masterList,userInput)==1 ):
                    return userInput
                    break
                else:
                    print("Between 1 and 50, Please")






                # isWork = True
        # while (isWork == True):
        #     userInput = input(self.getPlayer() + " what's your first Guess! It can be any Number 1 to 50")
        #     try:
        #         userInput = int(userInput)
        #     except:
        #         print("Can you please Insert a valid Number")
        #         continue
        #     if (searchList(self.masterList,userInput) != -1):
        #         return userInput
        #     else:
        #         print("Can you please Insert a valid Number")


    def playGame(self):
        print(self.getPlayer() + " are you ready for The First Round?!")
        input = self.getInput()
        print(input)
        if (searchList(self.WinningList, input) == 1):
            return 1
        else:
            print("Oooooo...Tough Luck Better Luck Next round...")
            print("It's Time for a 10 Secound Commercial Break!")
            time.sleep(1)
            print("This broadcast is brought to you by Chipotle")
            time.sleep(3)
            print("There's no-rovirus in the food this Time!")
            time.sleep(3)
            print("Disclamer: Guac is not free, don't get the chicken")
            time.sleep(1)
            print("And we're back")
            time.sleep(2)
            print(self.getPlayer() + " are you ready for The Secound Round?!")
            print("Let's Play!")
            input = self.getInput()
            print(input)
            if (searchList(self.WinningList, input) == 1):
                return 1
            else:
                print("Oooooo...Tough Luck Better Luck Next round...")
                print("Welcome to the third round!!!")
                time.sleep(1)
                print("Are you geting nervous?")
                time.sleep(1)
                print("Just guess one of 10 numbers and you win cash, it ain't rocket science!")
                time.sleep(1)
                print("Let's Play")
                input = self.getInput()
                print(input)
                if (searchList(self.WinningList, input) == 1):
                    return 1
                else:
                    return -1










def searchList(winArray, input):
    for i in range(len(winArray)):
        if winArray[i] == input:
            return 1
    return -1

def createWinningList(MasterList):
    # Used sample instead of Randrange to ensure no duplication of numbers and insure user get a fair shot
    winningList = random.sample(MasterList,10)
    return winningList
def runIntro():
    print("Welcome to ...")
    time.sleep(1)
    print("\nDrum roll please...")
    time.sleep(1)
    print("\n(Drum roll Sound) ")
    time.sleep(1)
    print("\n(Drum roll Sound) ")
    time.sleep(1)
    print("\n(Drum roll Sound) ")
    time.sleep(2)
    print("\nThe Number Guessing Game!!!")
    time.sleep(1)
    print("\n(Applause Sound) ")
    time.sleep(1)
    print("\nI'm Ben Sottile, your host")
    time.sleep(1)
    print("\nLet's play!")
    time.sleep(1)
def startGame(username):
    print("Welcome to the show " + username + "!!!")
    prompt = ""
    yes = ['yes', 'y']
    no = ['no', 'n']
    con = ['yes', 'y','no','n']
    while(prompt not in con):
        prompt = input("Have you seen our show before? [Insert y or n]")
        if prompt in yes:
            print("Then I won't waste anytime explaining the rules")
            time.sleep(1)
            print("Lets Get Right into it shall we?")
        elif prompt in no:
            print("I'll explain to you the game works then")
            time.sleep(1)
            print("You have three times to guess one of 10 lucky numbers, which can be anywhere from 1 to 50")
            time.sleep(2)
            print("If you manage to royally screw up 3 times you go home no richer than you were 30 seconds ago")
            time.sleep(2)
            print("Manage to Guess right however...")
            time.sleep(2)
            print("And you win $100!!!")
            print("Disclaimer: Redeemable after heat-death of sun...")
            time.sleep(1)
            print("Lets Get Right into it shall we?")
        else:
            print("Huh?" )

def main():
    import webbrowser
    runIntro()
    masterList = []
    for i in range(50):
        masterList.append(i+1)
    winningList = createWinningList(masterList)
    username = input("So what's your name champ?")
    username = username.upper()
    startGame(username)
    newGame = game(username,winningList,masterList)
    if (newGame.playGame() == 1):
        print("Oh, that's too bad...")
        time.sleep(3)
        print("That I just lost $100!")
        print("You've One The Show and $100 Congratulations!")
        wallet = open('Wallet', 'w+')
        wallet.write("This is $100!")
        wallet.write("Disclaimer: Only Valid at Chipotle and after the heat-death of sun")
        webbrowser.open('https://www.youtube.com/watch?v=GGXzlRoNtHU')
        print("Here were the Winning Numbers")
        print(winningList)
        print("")
    else:
        print("I'm sorry all you guesses are incorrect")
        print("Here were the Winning Numbers")
        print(winningList)
        time.sleep(1)
        print("If you want to earn a hundred dollars try...")
        print("[I've left something in your web browser]")
        webbrowser.open('https://careers.mcdonalds.com/main/')


main()