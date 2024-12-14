"""
This is a Python program allowing the user to access two different financial
calculators: an investment calculator and a home loan repayment calculator.
"""

# Import module
import math

def menu():
    # Display the user choices
    print("""\n===================================================================================
          \nMenu:
          \n> investment - to calculate the amount of interest you'll earn on your investment
          \n> bond       - to calculate the amount you'll have to pay on a home loan
          \n===================================================================================
          """)
    
    # Request user input
    while True:
        choice = input("""Enter either 'investment' or 'bond' from the menu above to proceed.
                       \nTo exit the program, enter 'quit': """).lower()
        if choice not in ("investment", "bond", "quit"):
            print("\n[!]: You did not enter 'investment', 'bond' or 'quit'.\n")
        else:
            break

    return choice

def investment():
    # Request and store user inputs
    while True:
        try:
            # P = The amount deposited
            P = float(input("\nEnter the amount of money you are depositing (omit £ symbol): "))
            # r = Rate of interest (%)
            r = float(input("Enter your interest rate (omit % symbol): "))/100
            # t = The amount of years planned to invest
            t = float(input("Enter the amount of years you plan to invest: "))
            break
        except ValueError:
            print("[!]: You have tried to enter a non-numerical character.")
    
    while True:
        interest = input("Enter either 'simple' or 'compound' interest: ").lower()
        if interest != "simple" and interest!= "compound":
            print("[!]: You did not enter either 'simple' or 'compound'.\n")
        else:
            break

    # Proceed according to the user's chosen interest type
    if interest == 'simple':
        # A = Total amount with added simple interest
        A = round(P * (1 + r*t),2)
        print(f"\nYour total amount once simple interest has been applied is £{A}.")

    else:
        # A = Total amount with added compound interest
        A = round(P * math.pow((1+r), t),2)
        print(f"\nYour total amount once compound interest has been applied is £{A}.")

def bond():
    # Request and store user inputs
    while True:
        try:
            # P = Present value of the house
            P = float(input("\nEnter the present value of the house (omit £ symbol): "))
            # i = Monthly interest rate
            i = float(input("Enter your yearly interest rate (omit % symbol): "))/100
            i = i/12
            # n = The number of months over which the bond will be repaid
            n = float(input("Enter the amount of months you plan to repay the bond: "))
            break
        except ValueError:
            print("[!]: You have tried to enter a non-numerical character.")
    
    # Calculate monthly repayment on home loan
    repayment = round((i*P)/(1 - (1+i)**(-n)),2)
    print(f"\nYou will have to repay £{repayment} each month.")

# Loop calculator until user chooses to quit
while True:
    choice = menu()
    if choice == "investment":
        investment()
    elif choice == "bond":
        bond()
    else:             
        break
    
