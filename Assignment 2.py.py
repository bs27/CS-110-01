# File name: Assignment 2
# Author Name: Ben Sottile
# Date: 09/12/2019
# Description: This code give a complete acurrate paycheck form for a set of inputs. Please note this is designed to
# work the same as the quickbooks software

# Welcome User Explain System

# get employee name
# get employee state

#Pay information
# get employee pay type
# get employee pay rate
# get how many hours employee worked
# Date employee was paid
# Insert type of pay period

#Additional Pay
# Insert ammount of overtime
#Insert Bonus pay
#Insert ammount of commision earned
#Insert Salary paid

#Insert Federal Tax Information
#Insert Filing Status
#Insert Number of Allowances
#Additional Witholding $$$

#Insert State Tax Information
#Insert Filing Status
#Insert Number of Allowances
#Additional Witholding $$$

#Do Calculations
#Gross pay is equal to the sum of your hourly wage times your hours worked + any additional income such as overtime earnings(overtime$=(pay*hours)*1.5), bonuses, commisions, and an additional sallary.
#Net pay is calculated as gross pay- the sum of the CA Income Tax(roughly Ten percent*Gross pay) Social Security(6.2*Gross pay) Federal Income tax(10*Gross pay) medicare=  (gross pay*1.45) calstate diability insurance (.01*gross pay)

#Do Output in Form use the print statement and concatination(for strings),
# commas for doubles. Follow Quickbooks Format- encompass style within print statement. use '''+insertStringVarHere+''' format
#to insert strings, use ''',insertNumVarHere,'''to insert doubles and ints

#import todays date for default purposes
from datetime import date
#prompt User
print('''                     Welcome to Ben.co's Paycheck Calculator!!!
                                Please enter all info as prompted
                                to ensure an accurate paycheck report

''')
#Get name
employeeName = "Bob Joe"
employeeName = (input("Please input your first and last name:  "))
#Get State Abbreviations
employeeState = "CA"
employeeState = (input('''
State	Abbreviation
ALABAMA	AL
ALASKA	AK
ARIZONA	AZ
ARKANSAS	AR
CALIFORNIA	CA
COLORADO	CO
CONNECTICUT	CT
DELAWARE	DE
FLORIDA	FL
GEORGIA	GA
HAWAII	HI
IDAHO	ID
ILLINOIS	IL
INDIANA	IN
IOWA	IA
KANSAS	KS
KENTUCKY	KY
LOUISIANA	LA
MAINE	ME
MARYLAND	MD
MASSACHUSETTS	MA
MICHIGAN	MI
MINNESOTA	MN
MISSISSIPPI	MS
MISSOURI	MO
MONTANA	MT
NEBRASKA	NE
NEVADA	NV
NEW HAMPSHIRE	NH
NEW JERSEY	NJ
NEW MEXICO	NM
NEW YORK	NY
NORTH CAROLINA	NC
NORTH DAKOTA	ND
OHIO	OH
OKLAHOMA	OK
OREGON	OR
PENNSYLVANIA	PA
RHODE ISLAND	RI
SOUTH CAROLINA	SC
SOUTH DAKOTA	SD
TENNESSEE	TN
TEXAS	TX
UTAH	UT
VERMONT	VT
VIRGINIA	VA
WASHINGTON	WA
WEST VIRGINIA	WV
WISCONSIN	WI
WYOMING	WY

Unincorporated organized territories
GUAM	GU
PUERTO RICO	PR
VIRGIN ISLANDS	VI



Please input your the two letter abbreviation of your state of residence  (^ ABBREVIATIONS ABOVE ^) : '''))
#Get pay information
print("PAY INFORMATION")

payType = "Hourly"

payType = (input("Are you paid hourly or a Salary?  :    "))
wage =0.00
wage =eval(input("How much are you paid in USD and hour  : $ "))
hoursWorked = 0
hoursWorked = eval(input("How many hours did you work: "))
payDate = date.today()
payDate = input("What date were you paid on? Please insert as DD/MM/YYYY :")
payPeriod = "Weekly"
payPeriod = input("On what basis are you paid Weekly or Bi-Weekly?:    ")
#Overtime Worked , Bonus $, Commission $ , Salary
#get additional pay info
print("Bonus Pay Information")
hoursWorkedOT = 0.00
hoursWorkedOT = eval(input("How many hours did you work Overtime: "))
bonusMoney = 0.00
bonusMoney = eval(input("How much did you make in monetary bonuses?: $ "))
commission = 0.00
commission = eval(input("How much did you make in any commission: $ "))
salaryEarned = 0.00
salaryEarned = eval(input("How much did you make in additional salary : $ "))

#Insert Federal Tax Information
print("Please insert the following Federal Tax Information ")
#Insert Filing Status
filingStatusF = "Single"
filingStatusF = (input("Please insert your filing status : "))
#Please insert number of allowances
allowanceNumF = 1
allowanceNumF = eval(input("Please insert number of tax allowances you noted on your W-4 form: "))
#Additional Witholding $$$
addWithF = 0.00
addWithF= eval(input("Please insert the amount you set to be withheld from your pay for Federal tax purposes on the W-4: $ "))

#Insert Federal Tax Information
print("Please insert the following State Tax Information ")
#Insert Filing Status
filingStatusS = "Single or Married(with two or more incomes"
filingStatusS = str(input("Please insert your filing status : "))
#Please insert number of allowances
allowanceNumS = 1
allowanceNumS = eval(input("Please insert number of tax allowances you noted: "))
#Additional Witholding $$$
addWithS = 0.00
addWithS= eval(input("Please insert the amount you set to be withheld from your pay for state tax purposes: "))
#Do Calculations
#Gross pay is equal to the sum of your hourly wage times your hours worked + any additional income such as overtime earnings
# (overtime$=(wage*hours)*1.5), bonuses, commisions, and an additional sallary.
#Net pay is calculated as gross pay- the sum of the CA Income Tax((roughly Ten percent*Gross pay)+withheldstate money)
# Social Security(6.2*Gross pay) Federal Income tax((.1*Gross pay)+witheld moneyfed) medicare=  (gross pay*1.45) calstate
# diability insurance (.01*gross pay)

grossPay = ((wage*hoursWorked)+((hoursWorkedOT*wage)*1.5)+bonusMoney+commission+salaryEarned)
# Quickbooks adds any additional withheld money into taxes totals applies for both state and fed)
caIncome = ((grossPay*.03)+addWithS)
fedIncome= (grossPay*0.0979+addWithF)
socialS = grossPay*.062
#Alright heres the deal this formula using my inputs should get the same thing on QB, however it should be noted that quickbooks
# determines federal income tax different for every input due to tax brakcets so it can't be 100

medicare = grossPay*.0145
calStateDI= grossPay*.01
netPay= grossPay-(caIncome+socialS+fedIncome+medicare+calStateDI)
payOT=(hoursWorkedOT*(wage*1.5))
payT= (hoursWorked*wage)
#Do Output in Form use the print statement and concatination(for strings),
# commas for doubles. Follow Quickbooks Format- encompass style within print statement. use '''+insertStringVarHere+''' format
#to insert strings, use ''',insertNumVarHere,'''to insert doubles and ints
print('''EMPLOYEE
Name : ''',employeeName,'''
Work State : ''',employeeState,'''
Pay Date : ''',payDate,'''
Pay Type : ''',payType,'''
Pay Period : ''',payPeriod,'''
Hours Worked : ''',hoursWorked,'''
Pay Rate : $''',wage,'''/ hour
Federal Filing Status : ''',filingStatusF,'''
Federal Exemptions : ''',allowanceNumF,'''
Federal Additional Withholding : ''',addWithF,'''
CA Filing status : ''',filingStatusS,'''
CA Number of Allowances : ''',allowanceNumS,'''
CA Additional Withholding : ''',addWithS,'''
PAYCHECK
Gross Pay : ''',grossPay,'''
Net Pay : $''',netPay,'''
Hourly : ''',payT,'''
Overtime : $''',payOT,'''
Salary : $''',salaryEarned,'''
Bonus : $''',bonusMoney,'''
Commission : $''',commission,'''
CA Income Tax : -$''',caIncome,'''
Social Security : -$''',socialS,'''
CA State Disability Ins : -$''',calStateDI,'''
Federal Income Tax : -$''',fedIncome,'''
Medicare : ''',medicare)



