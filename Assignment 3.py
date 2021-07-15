# File name: Assignment 3
# Author Name: Ben Sottile
# Date: 09/22/2019
# Description: This code prompts the user


#import math library
import math
def main():
#Main begins with user asked to input a number which will activate its respective math function via the if line.
    selection = int(input('''Please select your math function (Exit with 0) add = 1, sub = 2, mult = 3, divs = 4, sqrt = 5, sqred = 6,
    cubed = 7, x^y = 8, cubert = 9, nrt = 10, factorial= 11, log = 12, in= 13 , 10^x = 14, 1/x =15 sin = 16, cos = 17, tan = 18,
    sinh=19, cosh=20, tanh=21, inverse = 22, todegrees = 23, mod = 24  percent = 25 exp = 26'''))
    #if the user selects 0 main is not invoked to keep the calculator running and the goodbye my calculator line in printed.
    if selection == 0:
        print("Bye my calculator!")
    # the user is asked to insert two numbers which will be added
    if selection == 1:
       num1 = eval(input("First number? "))
       num2 =eval(input("Second number? "))
       sum = add(num1,num2)
       print(num1," + ", num2," = ",sum)
       main()
    #the user is asked to take two numbers and the secound is subtracted from the first.
    if selection == 2:
        num1 = eval(input("First number? "))
        num2 =eval(input("Second number? "))
        print(num1," - ", num2," = ", sub(num1, num2))
        main()
    #the user is asked to take two numbers which are multiplied together
    if selection == 3:
        num1 = eval(input("First number? "))
        num2 = eval(input("Second number? "))
        print(num1, " * ", num2, " = ", mult(num1, num2))
        main()
    #the user is asked to provide two numbers, the first one and the number it is divided by
    if selection == 4:
        num1 = eval(input("First number? "))
        num2 = eval(input("Second number? "))
        print(num1, " / ", num2, " = ", divs(num1, num2))
        main()
    # The user inserts a number and the square root of it is inserted
    if selection == 5:
        num1 = eval(input("Insert the number you want to take the square root of: "))
        print("The square root of ", num1 ,  " = ", sqrt(num1))
        main()
    # The user inserts a number and it is squared
    if selection == 6:
        num1 = eval(input("Insert the number you want to be squared: "))
        print( num1 ,  "^2 = ", sqred(num1))
        main()
    # The user inserts a number and it is cubed
    if selection == 7:
        num1 = eval(input("Insert the number you want to be cubed: "))
        print( num1 ,  " ^3 = ", cubed(num1))
        main()
    if selection == 8:
        num1 = eval(input("Insert the number : "))
        num2 = eval(input("Raised to what power? : "))
        print(num1 ,  "raised to the ", num2 , "th power = " , pow(num1,num2))
        main()
    # The user insert a number and the cube root is taken from it
    if selection == 9:
        num1 = eval(input("Insert number : "))
        print("The cube root of" , num1 , " = " , cbrt(num1))
        main()
    # the user insert a two numbers the first rooted by the secound
    if selection == 10:
        num1 = eval(input("Insert number : "))
        num2 = eval(input("Insert number : "))
        print("The" , num2 , "root of " , num1, "=" ,nrt(num1,num2))
        main()
    # the user inserts a number the factorials numerical vlsue is given
    if selection == 11:
        num1 = eval(input("Insert number : "))
        print("The" , num1 , "th factorial =" ,fac(num1))
        main()
    # the log10 of the given number is given
    if selection == 12:
        num1 = eval(input("Insert number : "))
        print("The log10", num1,"=" ,log(num1))
        main()
    # the log e of the given number is given.
    if selection == 13:
        num1 = eval(input("Insert number : "))
        print("The loge", num1,"=" , loge(num1))
        main()
    # 10 to the power of the number given is out putted
    if selection == 14:
        num1 = eval(input("Insert number : "))
        print("10^", num1,"=" , ten(num1))
        main()
    # 1/ the number given is outputed.
    if selection == 15:
        num1 = eval(input("Insert number : "))
        print("1/", num1," = " , ratio(num1))
        main()
    # the user inserts a number and the trigometic function of sine is applied
    if selection == 16:
        num1 = eval(input("Insert number : "))
        print("sin(", num1,") = " , sn(num1))
        main()
# the user inserts a number and the trigometic function of cosine is applied
    if selection == 17:
        num1 = eval(input("Insert number : "))
        print("cos(", num1,") = " , cs(num1))
        main()
# the user inserts a number and the trigometic function of tangent is applied
    if selection == 18:
        num1 = eval(input("Insert number : "))
        print("tan(", num1,") = " , tn(num1))
        main()
# the user inserts a number and the trigometic function of sineh is applied
    if selection == 19:
        num1 = eval(input("Insert number : "))
        print("sinh(", num1,") = " , snh(num1))
        main()
# the user inserts a number and the trigometic function of cosineh is applied
    if selection == 20:
        num1 = eval(input("Insert number : "))
        print("cosh(", num1,") = " , csh(num1))
        main()
# the user inserts a number and the trigometic function of tangenth is applied
    if selection == 21:
        num1 = eval(input("Insert number : "))
        print("tanh(", num1,") = " , tnh(num1))
        main()
# A user inserts a number and the additive and multplicative inverses are outputed
    if selection == 22:
        num1 = eval(input("Insert number : "))
        print("The additive and multiplicative inverse of" , num1," = " , inv(num1))
        main()
#the user inserts a number and it is converted to degrees
    if selection == 23:
        num1 = eval(input("Insert number : "))
        print( num1," to degrees =" , todegrees(num1))
        main()
# the user inserts two numbers and one number mods the other
    if selection == 24:
        num1 = eval(input("Insert number : "))
        num2 = eval(input("Insert number : "))
        print( num1,"%" ,num2, " = ", mod(num1,num2))
        main()
# the user enters two numbers and outout is the number that is the first number as a percent of the secound
    if selection == 25:
        num1 = eval(input("Insert number : "))
        num2 = eval(input("Insert number : "))
        print(num1, "% of", num2, " = ", per(num1, num2))
        main()
# the expodential form of the number inserted is given.
    if selection == 26:
        num1 = eval(input("Insert number : "))
        print(num1, "in exponential form = ", exp(num1))
        main()



def add(a,b):
    results = a + b
    return results
def sub(a,b):
     results = a - b
     return results
def mult(a,b):
    results = a * b
    return results
def divs (a,b):
    results = a / b
    return results
def sqrt(a):
    results = math.sqrt(a)
    return results
def sqred(a):
    results = math.pow(a,2)
    return results
def cubed(a):
    results = math.pow(a,3)
    return results
def pow(a,b):
    results = math.pow(a,b)
    return results
def cbrt(a):
    results = math.pow(a,(1/3))
    return results
def nrt(a,b):
    results = math.pow(a, (1 / (b)))
    return results
def fac(a):
        results= math.factorial(a)
        return results
def log(a):
    results = math.log10(a)
    return results
def loge(a):
    results = math.log(a , math.e)
    return results
def ten(a):
    results = math.pow(10,a)
    return results
def ratio(a):
    results = 1/a
    return results
def sn(a):
    result = math.sin(math.radians(a))
    return result
def cs(a):
    result = math.cos(math.radians(a))
    return result
def tn(a):
    result = math.tan(math.radians(a))
    return result
def snh(a):
    result = math.sinh(math.radians(a))
    return result
def csh(a):
    result = math.cosh(math.radians(a))
    return result
def tnh(a):
    result = math.tanh(math.radians(a))
    return result
def inv(a):
    result = -(a)
    result2 = 1/(a)
    return result, result2
def todegrees(a):
    result = math.degrees(a)
    return result
def mod(a,b):
    results= a%b
    return results
def per(a,b):
    results= (a*b)/100
    return results
def exp(a):
    results= math.exp(a)
    return results

main()
