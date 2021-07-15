# File name: Assignment 7
# Author Name: Ben Sottile
# Date: 10/19/2019
# Description: Will Search a car database and give users the car they want.


def main():
    print("Welcome to Big Bill's Hells Cars!\n")
    print("Time to find you a deal!\n")
    runSearchEngine()


def checkInputs(pL, ph, lowestPossiblePrice, highestPossiblePrice):
    if (pL < ph):
        if (int(ph) > int(lowestPossiblePrice)):
            if((int(pL)) > int(highestPossiblePrice)):
                print("Error Code 3: SO SORRY NONE of our cars were EXPENSIVE Enough for you! Try a Ferari dealer instead\n")
                main()
            else:
                return
        else:
            print("Error Code 2: Your too cheap\n")
            main()
    else:
        print("Error Code 1: Low Price Range Greater than High Price Range\n")
        main()


def checkMan(maker):
    maker = maker.lower()
    if (maker == "alfa-romero") or (maker == "audi") or (maker =="bmw")  or (maker =="chevrolet") or (maker == "dodge") or (maker == "honda") or (maker == "isuzu") or (maker =="jaguar") or (maker == "mazda") or (maker == "mercedes-benz") or (maker =="mitsubishi") or (maker == "nissan") or (maker =="porsche") or (maker =="toyota") or (maker =="volkswagen") or (maker == "volvo"):
        return
    else:
        print("We don't sell that kinda car here, so screwoff! \n")
        main()
# Search Engine
def runSearchEngine():

    fileNew = open("Automobile_data.csv", 'r')
    data = fileNew.read()
    itemizedList = data.split('\n')

    leng = len(itemizedList)
    index = []
    company = []
    bodystyle = []
    wheelbase = []
    length = []
    enginetype = []
    numofcylinders = []
    horsepower = []
    averagemileage = []
    price= []
    count = 0
    for num in itemizedList:
        i , c, bs, wb, l , et, nc, h, am, p = itemizedList[count].split(',')
        index.append(i)
        company.append(c)
        bodystyle.append(bs)
        wheelbase.append(wb)
        length.append(l)
        enginetype.append(et)
        numofcylinders.append(nc)
        horsepower.append(h)
        averagemileage.append(am)
        price.append(p)
        count += 1
    userInput = input(" Insert you price range (Lowest - Highest) : ")
    priceRangeLow, priceRangeHigh = userInput.split('-')
    priceRangeLow = int(priceRangeLow)
    priceRangeHigh = int(priceRangeHigh)
    del price[0]
    lowestPossiblePrice = 1000000
    for num in price:
        if (int(num) < int(lowestPossiblePrice)):
            lowestPossiblePrice = num
        else:
            continue
    highestPossiblePrice = 0
    for num in price:
        if (int(num) > int(highestPossiblePrice)):
            highestPossiblePrice = num
        else:
            continue
    checkInputs(priceRangeLow, priceRangeHigh,lowestPossiblePrice,highestPossiblePrice)
    count2 = 1
    priceMatch = []
    for num in price:
        if (priceRangeLow <= int(num) <= (priceRangeHigh)):
            priceMatch.append(count2)
            count2 +=1
        else:
            count2 += 1
    if (len(priceMatch) == 0):
        print(
            "No Cars Found. Too Bad. Maybe do as my mom says 'If you would broaden your standards you wouldn't be single\n")
        main()
    print(itemizedList[0])
    for x in priceMatch:
        print(itemizedList[x])

    manufacturer = input("These cars match your search\n"
                         "What brand were you looking for? : ")
    checkMan(manufacturer)
    manufacturer = manufacturer.lower()
    companyMatch = []
    for num in priceMatch:
        if ( company[num] == manufacturer):
            companyMatch.append(num)
        else:
            continue
    if (len(companyMatch) == 0):
        print(
            "No Cars Found. Too Bad. Maybe do as my mom says 'If you would broaden your standards you wouldn't be single'\n")
        main()
    print(itemizedList[0] + "\n")
    for x in companyMatch:
        print(itemizedList[x])

    file = open("YourSearchResults.csv", 'w')
    file.write('''Your search results: \n''' + itemizedList[0] + "\n")
    file.close()
    file = open("YourSearchResults.csv", 'a+')
    for x in companyMatch:
        file.write(itemizedList[x])
        file.write("\n")
    file.write("Please come Big Bill's Hells Cars Soon! "
               "Have you seen our ad?"
               "\nhttps://www.youtube.com/watch?v=-rsEs4HWXeY")
    file.close()
#     curtainCall()
# def curtainCall():
#     userInput2 = input("\nHave you seen our ad? Y/N" )
#     if (userInput2 == ("Y" or "y")):
#         print("\nWhy not see it again?")
#         webbrowser.open_new_tab(a_website)
#     elif (userInput2 == ("Y" or "y")):
#         print("\nAwesome give it a watch")
#         webbrowser.open_new_tab(a_website)
#     else:
#         print("\nNot Quite Sure what you said")
#         curtainCall()




main()


