# A = P(1 + r x t) simple interest
# A = P(1 + P)^t   compound interest

# R = (i x P) / (1 - i) ^ 9-n)) bond repayment

'''
P = present value
i = monthly interest rate (if i = 8 : i = (8/100) / 12 annual rate)
r = interest rate (if r = 8 : r = 8/100)
t = number of years for investment
n = number of months over the bond will be repaid
'''

'''
Pseudo
1. Display menu showing investment calculations for user.
2. Request user input for which calculation should be used.
   Display error, should incorrect input be detected.
   
3.  If user selects investment:
         request integers for investment calculation
         request user input for simple or compound interest.
         
    else:
        selected calculation is bond.
        request integers for bond repayment calculation.
        
4. Calculate final value for either investment ( A = P(1 + r x t) simple interest 
A = P(1 + P)^t compound interest) or bond (R = (i x P) / (1 - i) ^ 9-n)) bond repayment)

5. Display final result
'''
# importing math module for later calculations.
import math

# Display menu asking user for either investment or bond.
calc_selection = input(f''' 
Choose either 'investment' or 'bond' from the menu below to proceed : 

Investment - to calculate the amount of interest you'll earn on your investment 
Bond - to calculate the amount you'll have to pay on a home loan
''').lower()

# if statement to gather information for simple and compound investment calculations.
if calc_selection == "investment" :
    P = int(input("Please enter the amount you would like to invest : "))

    r = float(input("Enter the interest rate (do not include the % symbol): "))
    r= r / 100

    t = int(input("Enter the years you'd like to invest : "))

    invest = input("Please select simple or compound interest : ")

# if statement to calculate investment and return result to user.
    if invest == "simple":
        A = P*(1+r*t)
        print(A)

    elif  invest =="compound":
        A = P* math.pow((1+r),t)
        print(A)

# if statement to gather information for bond repayments.
if calc_selection == "bond":

    P = int(input("Please enter the present value of the house : "))

    i = float(input("Please enter the annual interest rate (do not include the % symbol) : "))/12

    n = int(input("Please enter the number of months over which the bond will be repaid :"))

# if statement to calculate bond repayments and return result to user.
if calc_selection == "bond":
    R = (i*P)/(1 - (1+i)**(-n))
    print(R)

# will terminate if given wrong input.
else:
    print("invalid input . . . terminating ")


