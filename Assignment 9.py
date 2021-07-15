# File name: Assignment 9
# Author Name: Ben Sottile
# Date: 11/3/2019
# Description: This is a simulation of the Skunk Dice Game
# The object of the game is to be the first player to score 75 points (or more) and not have their total score beaten.  This is entertainingly done by the rolling of two six sided dice. The number one is considered the skunk.
# A player scores points by rolling the dice and adding together their total. For example if a player rolls a 6 and 5, their score would be 11.  They can choose to roll again and continue to add to this score, taking the risk of rolling a skunk, or they can stop and keep the score of 11 for their first round.
# Rolling a skunk or double skunks during a players turn has consequences.  If the player rolls one skunk at anytime during their turn, they receive 0 points for the round.   If a player rolls double skunks at anytime during their turn, they receive a 0 for the round and all the previous rounds.  They need to start all over again in accumulating points.
# So, in the above example, if the player with the score of 11 chose to roll again and then rolled a 3 and an image of a skunk, their turn would end and they would receive 0 points.  Double skunks would wipe out their entire score.
# Once a player reaches 100 points that player can continue to roll raising the ‘goal’ or immediately stop.  The other players are given one more chance to reach the goal and possibly even win the game.
# With every roll the odds of rolling a skunk or skunks increases.  Players may soon learn to go steady like a turtle and accept their measly one roll scores of anywhere between 4 and 12.  Or for some players, the temptation is too great and they continue to roll to see how high they can go.
# They take the advice of the skunks.   Written on the box, the adorable skunks are quoted and urging players on; “Come on, take another shake” or “Don’t be afraid of a little skunk!”
# This all makes for great family fun on game night.   Older children or adults can help the younger children add their totals and ask them if they want to roll again.  They know if they see a ‘Skunk’ their turn will end but the image of the skunk will still make them smile.
# And because of the entertaining quality of risk playing, all players enjoy watching the rolls of the skunk dice!
import random
import time
class Dice:
    def __init__(self):
        self.dice = [0]*2
        self.rollAll()
    def roll(self , which):
        for pos in which:
            self.dice[pos] = random.randrange(1,7)
    def rollAll(self):
        self.roll(range(2))
    def display(self):
        return self.dice[:]

class player:
    def __init__(self,userName, score):
        self.userName = str(userName)
        self.score = score

    def getScore(self):
        return self.score
    def getUserName(self):
        return self.userName
    def setScore(self,score):
        self.score = int(score)
    def roundGo(self):
        con = ['y', 'yes','n', 'no']
        yes = ['y', 'yes']
        no = ['n', 'no']
        time.sleep(1)
        userInput = input("Would you like to continue? Please insert y / n ?")
        userInput = userInput.lower()
        while (userInput not in con):
            userInput = input("Would you like to continue? Please insert y / n ?")
            userInput = userInput.lower()
        if userInput in yes:
            time.sleep(1)
            print('''Good Luck then! \n''')
            return True
        elif userInput in no:
            time.sleep(1)
            print("\nPlaying it Safe?...Wuss")
            return False
        else:
            print("")


    def newScore(self):
        print(self.getUserName())
        userInput = input("New Score:")
        self.setScore(userInput)

    def startRound(self, dice):
        print("Welcome! " + self.getUserName())
        roundScore = 0
        totalScore = self.getScore()
        roundContinue = 1
        dice.rollAll()
        print("Your roll for this round have come as :")
        time.sleep(1)
        print(dice.display())
        if(dice.display() == [1,1]):
            time.sleep(1)
            print("BUT, TOO BAD you rolled a DOUBLE SKUNK! ")
            roundScore = 0
            totalScore = 0
            self.setScore(0)
        elif 1 in dice.display():
            time.sleep(1)
            print("BUT, TOO BAD you rolled a Single Skunk")
            roundScore = 0
        else:
            for num in dice.display():
                roundScore = roundScore + num
            while (roundContinue == 1):
                print("Your score for this round is", roundScore)
                time.sleep(1)
                print("Your banked total is", self.getScore())
                keepGoing = self.roundGo()
                if keepGoing == True:
                    dice.rollAll()
                    print("Your roll for this round have come as :")
                    time.sleep(1)
                    print(dice.display())
                    if (dice.display() == [1,1]):
                        time.sleep(1)
                        print("BUT, TOO BAD you rolled a DOUBLE SKUNK! ")
                        roundScore = 0
                        totalScore = 0
                        roundContinue = 0
                        self.setScore(0)
                    elif 1 in dice.display():
                        time.sleep(1)
                        print("BUT, TOO BAD you rolled a Single Skunk")
                        roundScore = 0
                        roundContinue = 0
                    else:
                        for num in dice.display():
                            roundScore = roundScore + num
                elif keepGoing == False:
                    roundContinue = 0
                else:
                    print("Not Sure what you said")
            print(self.getUserName() + "'s Score for this round is ", roundScore)
            totalScore = totalScore + roundScore
            self.setScore(totalScore)
            time.sleep(1)
            print(self.getUserName() + "'s Total ", self.getScore())
def showRules():
    yes = ['y','yes']
    no = ['n' ,'no']
    userInput = input("Would you like to see the rules? Please insert y / n ?")
    userInput = userInput.lower()
    if userInput in yes:
        print('''
GOAL OF GAME- Be the first player to score 100 points (or more) and not have their total score beaten.''')
        time.sleep(3)
        print('''
SET UP - To play get two players and this Skunk simulator program.
        ''')
        time.sleep(3)
        print('''
GAMEPLAY - To win you will roll two six sided dice and add the total numerical values to your total.
The player who has chosen to be PLAYER ONE will roll. For example if a player rolls a 6 and 5, their score would be 11.
They can choose to roll again and continue to add to this score, taking the risk of rolling a 'skunk', or they can stop 
and keep the score of 11 for their first round.The player can either decide to roll again or pass the dice to PLAYER TWO. 
PLAYER TWO will then roll, add to their total score and can either roll again or pass the dice back to PLAYER ONE. 
                ''')
        time.sleep(5)
        print('''
ENDGAME -The game countiues until one player passes the dice with a score at or over the target score. Once a player reaches the target score that player can continue 
to roll raising the ‘goal’ or immediately stop. The other player is given one more chance to reach the goal and 
possibly even win the game. With every roll the odds of rolling a skunk or skunks increases.
                ''')
        time.sleep(5)
        print('''ROLLING A SKUNK - A 'SKUNK' is rolled when one or more one values are rolled. Rolling a skunk or double skunks during a players turn has consequences.  
If the player rolls one skunk at anytime during their turn, they receive 0 points for the round and the dice is passed to the other player.  
If a player rolls double skunks at anytime during their turn, they receive a 0 for the round and their total score is brought to zero.  
They need to start all over again in accumulating points. So, if the player with the score of 11 chose to roll again and then rolled a 3 and a 1, 
their turn would end and they would receive 0 points. Double skunks would wipe out not only the 11 points for this round, but any points they 
have stored up from other rounds.

Scroll up to see the full rules ''')
        time.sleep(5)
        print('''
You Ready?''')
        time.sleep(2)
        print('''
I don't care if are or aren't, 

LETS START THE GAME ! ! !''')
    elif userInput in no:
        print("\nOkay then let's start the game!")
    else:
        print("I don't understand what you said.")
        showRules()

def main():
    print('''
------ Welcome to Skunk! ------
    
Note: This is a two player game.

''')
    showRules()
    userNameOne = input("\n PLAYER ONE - What is your name? :")
    playerOne = player(userNameOne,0)
    userNameTwo = input("\n PLAYER TWO - What is your name? :")
    playerTwo = player(userNameTwo,0)
    dice = Dice()
    con = True
    print("-----Welcome " + playerOne.getUserName()+ " ------")
    print("-----Welcome " + playerTwo.getUserName() + " ------")
    print('''
What type of game would you like to play? (Insert 1,2,3):
1 - Quick Game : Target Score = 50
2 - Medium Game: Target Score = 75
3 - Full Game  : Target Score = 100
Warning: Full Game will take quite a long time!!!
''')
    while (con==True):
        userInput = input("Select a Game Mode: ")
        try:
            choice = int(userInput)
        except ValueError:
            continue
        if choice == 1:
            maxScore = 49
            con = False
            break
        if choice == 2:
            maxScore = 74
            con = False
            break
        if choice == 3:
            maxScore = 99
            con = False
            break
    gameOn = 1
    while (gameOn == 1):
        if playerTwo.getScore() > maxScore:
            maxScore = playerTwo.getScore()
            gameOn = 0
            playerOne.startRound(dice)
            playerOne.newScore()
            if playerTwo.getScore() == playerOne.getScore():
                print("----Game Over----")
                print(playerTwo.getUserName() + " Wins!!!")
                print(playerOne.getUserName() + " Failed to Beat the goal!")
                print("Results: ")
                print(playerOne.getUserName() + " : ", playerOne.getScore())
                print(playerTwo.getUserName() + " : ", playerTwo.getScore())
                gameOn = 0
        else:
            playerOne.startRound(dice)
        if gameOn == 1:
            if playerOne.getScore() > maxScore:
                maxScore = playerOne.getScore()
                gameOn = 0
                playerTwo.startRound(dice)
                if playerTwo.getScore() == playerOne.getScore():
                    print("----Game Over----")
                    print(playerOne.getUserName() + " Wins!!!")
                    print(playerTwo.getUserName() + " Failed to Beat the goal!")
                    print("Results: ")
                    print(playerOne.getUserName() + " : ", playerOne.getScore())
                    print(playerTwo.getUserName() + " : ", playerTwo.getScore())
            else:
                playerTwo.startRound(dice)
        else:
            print("")
    if playerOne.getScore() > playerTwo.getScore():
        print("----Game Over----")
        print(playerOne.getUserName() + " Wins!!!")
        print(playerTwo.getUserName() + " Failed to Beat the goal!")
        print("Results: ")
        print(playerOne.getUserName() + " : ",playerOne.getScore())
        print(playerTwo.getUserName()+ " : ",playerTwo.getScore())
    if playerOne.getScore() < playerTwo.getScore():
        print("----Game Over----")
        print(playerTwo.getUserName() + " Wins!!!")
        print(playerOne.getUserName() + " Failed to Beat the goal!")
        print("Results: ")
        print(playerOne.getUserName() + " : ",playerOne.getScore())
        print(playerTwo.getUserName()+ " : ",playerTwo.getScore())
main()