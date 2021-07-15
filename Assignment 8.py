# # File name: Assignment 8
# # Author Name: Ben Sottile
# # Date: 10/25/2019
# # Description:
# Upload Assignment: assignment 8
#    ASSIGNMENT INFORMATION
# Due Date
# Sunday, October 27, 2019
# 11:59 PM
# Points Possible
# 20
# Design a code for ATM machines that can work for chase bank. In real life the ATM machine connects to the chase bank data base to access each customer information. In here download the csv file and your data base. Each customer has a account number, name, account password and outstanding balance.
#
# Your code should ask the use to login with typing their account# and Pin#. If they entered correct information, then the customer has access to the bank system to deposit or  withdraw money. Exit the program after 3 retires if the customer enters them incorrectly the first time.
#
# They can't  withdraw more than what they have in their account.
#
# Update the csv file with new balance each time a transaction happens.
#
# Output their statement to the screen and write it to a file called statement.csv.
#
# Turn in your code, output screen shot and statement.csv.
#
# Note: Your code must have a class for the bank with at least two methods (deposit and  withdraw).
class bank:
    def __init__(self, accountNum, name ,pin ,balance):
        self.accountNum = accountNum
        self.name = name
        self.pin = pin
        self.balence = balance
    def getAccountNum(self):
        return self.accountNum
    def getName(self):
        return self.name
    def getPin(self):
        return self.pin
    def getBalence(self):
        return self.balence
    def makeStatement(self):
        print('''
        ---------------Chase Bank------------------
        Account Number : ''' + self.accountNum + '''
        User : ''' + self.getName() + '''
        Current Balence: $''' , self.getBalence())
    def deposit(self):
        userInput = input('''Please insert the amount you  will be entrusting with us today. 
                     Deposit Amount: $ ''')
        if (userInput == 0):
            print("Error")
        try:
            userInput = float(userInput)
        except:
            userInput = ""
        if not type(userInput) is float:
            print("Wrong type Inserted!")
            self.deposit()
        self.balence = float(self.balence) + userInput
        print("Your Account has been updated")
        self.makeStatement()
        print('''        Original Balence''', (self.balence - userInput))
        print('''        Deposit : +$ ''',userInput)
        print("Thanks again for entrusting your money with chase bank!")
        superStatement(self.accountNum, self.name, (self.balence - userInput),self.balence, userInput)

    def withdrawl(self):
        print('''Please insert the amount you want to get from your account of $ ''',self.balence)
        userInput = input('''Withdrawl Amount: $ ''')
        if (userInput == 0):
            print("Error")
        try:
            userInput = float(userInput)
        except:
            userInput = ""
        if not type(userInput) is float:
            print("Wrong type Inserted!")
            self.withdrawl()

        if (float(userInput) > float(self.balence)):
            print("Insufficient Funds to process request\n")
            self.withdrawl()
        else:
            self.balence = float(self.balence) - userInput
            print("Your Account has been updated")
            self.makeStatement()
            print('''        Original Balence''', (self.balence + userInput))
            print('''        Withdrawl : -$ ''', userInput)
            superStatement(self.accountNum, self.name, (self.balence + userInput),self.balence, userInput)


def rewrite(index, newBalence ):
    data = open("Bank_Data_Base.csv", 'r',)
    accountNumber = []
    name = []
    pin = []
    balence = []
    aN = ''
    n = ''
    pin2 = ''
    b = ''
    count = 0
    for line in data:
        count =+ 1
        aN , n , pin2 , b = line.split(',')
        accountNumber.append(aN)
        name.append(n)
        pin.append(pin2)
        balence.append(b)
    balence[index-1] = newBalence
    data.close()
    data2 = open("Bank_Data_Base.csv", 'w')
    for i in range(20):
        theInput = str(accountNumber[i])+','+ name[i] + ',' + str(pin[i]) + ',' + str(balence[i])
        data2.write(theInput)
        if (i == index-1):
            data2.write("\n")
    #Add Deposit Withdrawl with Limi
    data2.close()
def makeBank(accountInfo):
    accountNum, name, pin, balance = accountInfo.split(',')
    return bank(accountNum, name, pin, balance)
def superStatement(accountNum, name, originalBalence, newBalence, userInput):
    data2 = open("statement.csv", 'w')
    data2.write(''''---------------Chase Bank------------------''')
    data2.write("\n")
    data2.write(str('''Account Number : '''+ name))
    data2.write("\n")
    data2.write(str('''User :''' + name))
    data2.write("\n")
    data2.write('''Current Balence: ''')
    data2.write("\n")
    data2.write(str(newBalence))
    data2.write("\n")
    data2.write(str("Change :"))
    data2.write("\n")
    data2.write(str(userInput))
    data2.write("\n")
    data2.write(str('''Original Balence: $'''))
    data2.write("\n")
    data2.write(str(originalBalence))
    data2.close()

def promptUser():
    print("")
    userInput = input( '''What are you intrested in doing to day? Your options are below
                      Withdrawl Funds - Press 1
                      Deposit Funds   - Press 2''')
    try:
        userInput = int(userInput)
    except:
        userInput = ""
    if not type(userInput) is int:
        print("We aren't sure what service you want - Please try again")
        promptUser()
    else:
        if int(userInput) == 1:
            return True
        elif (userInput) == 2:
            return False
        else:
            print("\n We aren't sure what service you want - Please try again")
            promptUser()
def main():
    print("Welcome to chase Bank! We kill the Competition! A total legal bank that isn't FDIC Insured or a Mob Front!")
    index , con , correctBankAccount = checkShit()
    if (con == True):
        allData = open("Bank_Data_Base.csv",'r')
      #  info = allData.readline(index,index)
      #  correctBankAccount = makeBank(info)
        allData.close()
    else:
        print("")
        exit()
    correctBankAccount.makeStatement()
    print("Welcome Back to Chase Bank Valued Customer! \n")
    x = promptUser()
    if (x == True):
        print("Withdrawl Function Selected \n")
        correctBankAccount.withdrawl()
        rewrite(index, correctBankAccount.getBalence())
    elif(x == False):
        print("Deposit Function Selected \n")
        correctBankAccount.deposit()
        rewrite(index, correctBankAccount.getBalence())
    else:
        print("Yeah I'm not really sure how you ended up here...Hacker!")


def checkShit():
    automaticInstaDeathSecurityCounter = 0

    while (automaticInstaDeathSecurityCounter < 3):
        allData = open("Bank_Data_Base.csv", 'r')
        print("Time to Login..."
              "Be aware you currently have",(3-automaticInstaDeathSecurityCounter), " try's left until the autosecurity system activates. "
                                              "Full Disclosure: You will die")
        userAccountNumber = input("What is your AccountNumber?")
        userPINNumber = input("What is your Pin?")
        count = 0
        for line in allData:
            if line == 0:
                count += 1
                continue
            else:
                count += 1
                theOne = makeBank(line)
                if (theOne.getAccountNum() == userAccountNumber) and (theOne.getPin() == userPINNumber):

                    return count , True , theOne
                else:
                    continue
        automaticInstaDeathSecurityCounter += 1
        allData.close()
    print("You Have Failed. Security system activated. You should start running ")
    accountInfo = "0000000,Empty,hello123,200"
    return 0,False , makeBank(accountInfo)
main()






