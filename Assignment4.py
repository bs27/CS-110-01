def main():
    print("Welcome to Ben.co's Day of the Year calculator. Please enter the year and we'll give you the corresponding"
          "day number. Example: March 17, 2000 = 77 ")
    dataInput = input("Please insert date of your choosing in the format: MM/DD/YYYY. ")
    month, day, year = dataInput.split("/")
    month = (int(month))
    day = (int(day))
    year = (int(year))
    if (isValid(month, day, year)==1):
        print("The day number=", calc(month, day, year))

    else :
        print("")


def roundfix(num1):
    if ((num1%1) != 0):
        num1 = int(num1) +1
        return num1
    else:
        return num1



def isValid(month, day , year):
    endProgram= 0
    if(isValidDay(month, day,year)== 0):
        print("Day of Month invalid")
        endProgram = 1
    if (isValidMonth(month) == 0):
        print("Month invalid")
        endProgram = 1
    if (isValidYear(year) == 0):
        print("Year invalid")
        endProgram = 1
    if endProgram== 1:
        results = 0
        return results
    else:
        results = 1
        return results


def isValidDay(month, day , year):
    if(day>31):
        return 0
    else:
        if (month == (1 or 3 or 5 or 8 or 7 or 10 or 12)):
            if (0 < (day) <= 31):

                return 1
            else:
                return 0
        elif (month == (4 or 6 or 9 or 11)):
            if (0 < day <= 30):
                return 1
            else:
                return 0
        elif (month == 2):
            if ((year % 4) == 0):
                if (0 < day <= 29):
                    return 1
                else:
                    return 0
            else:
                if (0 < day < 29):
                    return 1
                else:
                    return 0


def isValidYear(year):
    if (0<=year<=9999):
        results= 1
        return results
    else:
        results = 0
        return results
def isValidMonth(month):
    if (0<month<13):
        results= 1
        return results
    else:
        results = 0
        return results
def calc(month, day , year):
    if(month>2):
        num2 = (4 * month + 23)/10
    else:
        num2=0
    answer = ((31 * (month-1)) + day) - num2
    answer = roundfix(answer)
    if ((month>2) and (year%4==0)):
        answer = answer + 1
        return answer
    else:
        return answer


main()
