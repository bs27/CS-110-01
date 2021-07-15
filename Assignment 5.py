# File name: Assignment 5
# Author Name: Ben Sottile
# Date: 10/6/2019
# Description: This code prompts the user what math function they want and performs it for them.

# import math library
import math
# Sorry Professor if Varriable names are confusing I reused a lot of code. However it works efficiently and I refuse to mess with greatness!
def main():

    # Main begins with user asked to input a number which will activate its respective math function via the if line.
    selection = int(input('''Please select your math function (Exit with 0) add = 1, sub = 2, mult = 3, divs = 4, sqrt = 5, sqred = 6,
    cubed = 7, x^y = 8, cubert = 9, nrt = 10, factorial= 11, log = 12, in= 13 , 10^x = 14, 1/x =15 sin = 16, cos = 17, tan = 18,
    sinh=19, cosh=20, tanh=21, inverse = 22, todegrees = 23, mod = 24  percent = 25 exp = 26 : '''))
    # if the user selects 0 main is not invoked to keep the calculator running and the goodbye my calculator line in printed.
    if selection == 0:
        print("Bye my calculator!")
    # the user is asked to insert two numbers which will be added
    if selection == 1:
        x = []
        n=1
        firstNum = (input("Number to be added to?"))
        firstNum = float(firstNum)
        x.append(float(firstNum))
        secound = (input("Secound number to be added to first?"))
        x.append(float(secound))
        while(n==1):
            numNew = (input("= or countinue to add new number?"))
            sum = 0
            if(numNew == "="):
                print(add(x))
                break
            else:
                x.append(float(numNew))

        main()

    # the user is asked to take two numbers and the secound is subtracted from the first.
    if selection == 2:
        x = []
        n = 1
        firstNum = (input("Number to be subtracted from?"))
        firstNum= float(firstNum)
        subtract= (input("Secound number?"))
        x.append(float(subtract))
        while(n==1):
            numNew = (input("= or countinue to sub new number?(insert new number to sub from result)"))
            if (numNew == "="):
                print(sub(firstNum, x))
                break
            else:
                x.append(float(numNew))


        main()
    # the user is asked to take two numbers which are multiplied together
    if selection == 3:
        x = []
        n = 1
        firstNum = (input("Number to be multiplied?"))
        firstNum = float(firstNum)
        subtract = (input("Number to be multiplyed by"))
        x.append(float(subtract))
        while (n == 1):
            numNew = (input("= or countinue to mult result?(insert new number to mult by result)"))
            if (numNew == "="):
                print(mult(firstNum, x))
                break
            else:
                x.append(float(numNew))

        main()
    # the user is asked to provide two numbers, the first one and the number it is divided by
    if selection == 4:
        x = []
        n = 1
        firstNum = (input("Number?"))
        firstNum = float(firstNum)
        subtract = (input("Number to divide the first number by"))
        x.append(float(subtract))
        while (n == 1):
            numNew = (input("= or countinue to divide result?(insert new number to divide by result)"))
            if (numNew == "="):
                print(divs(firstNum, x))
                break
            else:
                x.append(float(numNew))

        main()
    # The user inserts a number and the square root of it is inserted
    if selection == 5:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to be sqrted?"))
        firstNum = float(firstNum)
        while (n == 1):
            print("Number Square rooted:")
            print(sqrt(firstNum, x))
            numNew = (input("Contiune to sqrt? (1 or 0)"))
            if (numNew == "0"):
                break
            elif(numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # The user inserts a number and it is squared
    if selection == 6:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to be sqred?"))
        firstNum = float(firstNum)
        while (n == 1):
            print("Number Squared:")
            print(sqred(firstNum, x))
            numNew = (input("Contiune to sqred? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # The user inserts a number and it is cubed
    if selection == 7:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to be cubed?"))
        firstNum = float(firstNum)
        while (n == 1):
            print("Number cubed:")
            print(cubed(firstNum, x))
            numNew = (input("Contiune to cubed? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    if selection == 8:
        x = []
        n = 1
        firstNum = (input("Number to be raised to a power?"))
        firstNum = float(firstNum)
        power = (input("Power?"))
        x.append(float(power))
        while (n == 1):
            print("Result:")
            print(pow(firstNum, x))
            numNew = (input("Contiune to raised to a power (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                power = (input("Power?"))
                x.append(float(power))
            else:
                print("Error")

        main()
    # The user insert a number and the cube root is taken from it
    if selection == 9:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to be cbrt?"))
        firstNum = float(firstNum)
        while (n == 1):
            print("Number cbrt:")
            print(cbrt(firstNum, x))
            numNew = (input("Contiune to cbrt? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # the user insert a two numbers the first rooted by the secound
    if selection == 10:
        x = []
        n = 1
        firstNum = (input("Number to be rooted by a number?"))
        firstNum = float(firstNum)
        power = (input("root?"))
        x.append(float(power))
        while (n == 1):
            print("Result:")
            print(nrt(firstNum, x))
            numNew = (input("Contiune to be rooted (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                power = (input("root?"))
                x.append(float(power))
            else:
                print("Error")

        main()
    # the user inserts a number the factorials numerical vlsue is given
    if selection == 11:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to be ! ?"))
        firstNum = float(firstNum)
        while (n == 1):
            print("Number ! :")
            print(fac(firstNum, x))
            numNew = (input("Contiune to fac? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # the log10 of the given number is given
    if selection == 12:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to be log10 ?"))
        firstNum = float(firstNum)
        while (n == 1):
            print("Number log10 :")
            print(log(firstNum, x))
            numNew = (input("Contiune to log? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # the log e of the given number is given.
    if selection == 13:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to be in ?"))
        firstNum = float(firstNum)
        while (n == 1):
            print("loge Number  :")
            print(loge(firstNum, x))
            numNew = (input("Contiune to loge? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # 10 to the power of the number given is out putted
    if selection == 14:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("10 to the what power?"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" Number^10 :")
            print(ten(firstNum, x))
            numNew = (input("Raise 10 to result? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # 1/ the number given is outputed.
    if selection == 15:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("1/ what number? "))
        firstNum = float(firstNum)
        while (n == 1):
            print(" 1/number :")
            print(ratio(firstNum, x))
            numNew = (input("Ratio again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")


        main()
    # the user inserts a number and the trigometic function of sine is applied
    if selection == 16:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Sine of what number in radians"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" sine(number) :")
            print(sn(firstNum, x))
            numNew = (input("Sn again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")


        main()
    # the user inserts a number and the trigometic function of cosine is applied
    if selection == 17:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Cosine of what number in radians"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" Cosine(number) :")
            print(cs(firstNum, x))
            numNew = (input("cs again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")



        main()
    # the user inserts a number and the trigometic function of tangent is applied
    if selection == 18:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Tangent of what number in radians"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" Tangent(number) :")
            print(tn(firstNum, x))
            numNew = (input("Tn again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")


        main()
    # the user inserts a number and the trigometic function of sineh is applied
    if selection == 19:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Sinh of what number in radians"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" Sinh(number) :")
            print(snh(firstNum, x))
            numNew = (input("Snh again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")


        main()
    # the user inserts a number and the trigometic function of cosineh is applied
    if selection == 20:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Cosh of what number in radians"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" cosh(number) :")
            print(cosh(firstNum, x))
            numNew = (input("Cosh again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")


        main()
    # the user inserts a number and the trigometic function of tangenth is applied
    if selection == 21:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Tanh of what number in radians"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" Tanh(number) :")
            print(tnh(firstNum, x))
            numNew = (input("Tanh again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # A user inserts a number and the additive and multplicative inverses are outputed
    if selection == 22:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Additive and Multiplicative inverse of what number?"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" Additive and Multiplicative inverse:")
            print(inv(firstNum, x))
            numNew = (input("Get Inverses again? (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()
    # the user inserts a number and it is converted to degrees
    if selection == 23:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Convert Number to Degrees"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" convert to degrees (number) :")
            print(todegrees(firstNum, x))
            numNew = (input("Convert to degrees again? (1 or 0) Hint: Genius, it will treat your new answer as radians again"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")


        main()
    # the user inserts two numbers and one number mods the other
    if selection == 24:
        x = []
        n = 1
        firstNum = (input("Number?"))
        firstNum = float(firstNum)
        subtract = (input("Number to mod the first number by"))
        x.append(float(subtract))
        while (n == 1):
            numNew = (input("= or countinue to mod result?(insert new number)"))
            if (numNew == "="):
                print(mod(firstNum, x))
                break
            else:
                x.append(float(numNew))


        main()
    # the user enters two numbers and outout is the number that is the first number as a percent of the secound
    if selection == 25:
        x = []
        n = 1
        firstNum = (input("Number?"))
        firstNum = float(firstNum)
        power = (input("What % of that number"))
        x.append(float(power))
        while (n == 1):
            print("Result:")
            print(per(firstNum, x))
            numNew = (input("Contiune to take % of result (1 or 0)"))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                power = (input("% of result?"))
                x.append(float(power))
            else:
                print("Error")



        main()
    # the expodential form of the number inserted is given.
    if selection == 26:
        x = ["Placeholder"]
        n = 1
        firstNum = (input("Number to take to expodential?"))
        firstNum = float(firstNum)
        while (n == 1):
            print(" Number to exp (number) :")
            print(exp(firstNum, x))
            numNew = (input("exp results again? (1 or 0) "))
            if (numNew == "0"):
                break
            elif (numNew == "1"):
                x.append("Placeholder")
            else:
                print("Error")

        main()


def add(x):
    sum = 0
    for myVar in x:
        sum = sum + myVar
    return sum

def sub(a, b):
    num = a
    for myVar in b:
        num = num - myVar
    return num

def mult(a, b):
    num = a
    for myVar in b:
        num = num * myVar
    return num

def divs(a, b):
    num = a
    for myVar in b:
        num = num / myVar
    return num

def sqrt(a, x):
    results = a
    for myVar in x:
        results = math.sqrt(results)
    return results

def sqred(a, x):
    results = a
    for myVar in x:
        results = math.pow(results, 2)
    return results

def cubed(a, x):
    results = a
    for myVar in x:
        results = math.pow(results, 3)
    return results

def pow(a, x):
    results = a
    for myVar in x:
        results = math.pow(results, myVar)
    return results


def cbrt(a, x):
    results = a
    for myVar in x:
        results = math.pow(results, 1/3)
    return results

def nrt(a, b):
    results = a
    for myVar in b:
        results = math.pow(results, 1/(myVar))
    return results

def fac(a, b):
    results = a
    for myVar in b:
        results = math.factorial(results)
    return results

def log(a, b):
    results = a
    for myVar in b:
        results = math.log10(results)
    return results

def loge(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.log(results, math.e)
    return results

def ten(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.pow(10, results)
    return results

def ratio(firstNum, x):
    results = firstNum
    for myVar in x:
        results = 1/results
    return results

def sn(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.sin(math.radians(results))
    return results

def cs(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.cos(math.radians(results))
    return results

def tn(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.tan(math.radians(results))
    return results

def snh(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.sinh(math.radians(results))
    return results

def cosh(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.cosh(math.radians(results))
    return results

def tnh(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.tanh(math.radians(results))
    return results

def inv(firstNum, x):
    results1 = firstNum
    results2 = firstNum
    for myVar in x:
        results1 = -(results1)
        results2 = 1 / (results2)
    return results1, results2

def todegrees(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.degrees(results)
    return results

def mod(a, b):
    num = a
    for myVar in b:
        num = num % myVar
    return num

def per(firstNum, x):
    results = firstNum
    for myVar in x:
        results = (results * myVar) / 100
    return results

def exp(firstNum, x):
    results = firstNum
    for myVar in x:
        results = math.exp(results)
    return results

main()
