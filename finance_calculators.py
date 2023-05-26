# Capstone Project I — Variables and Control Structures
import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n")
# \n, used at the end, produces the empty line asked in the task descriotion
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

# To make sure the capitalisation of the selection would not affect the program process:
choice = choice.lower()

if choice == "investment":
    deposit = float(input("Enter the amount of money that you are depositing : "))
    interest_rate = float(input("Enter the interest rate (as a percentage) : "))
    # to deal with the % we can get the input as:
    # interest_rate = input("Enter the interest rate (as a percentage) : ")
    # interest_rate = interest_rate.strip("%")
    # interest_rate = float(interest_rate)
    
    duration = float(input("Enter the number of years you plan on investing : "))
    interest = input("Do want \"simple\" or \"compound\" interest : ").lower()
    # Again .lower() function has been used to deal with the capitalisation
    if interest == "simple":
        final_amount = deposit*(1 + (interest_rate/100)*duration)
        print(f"You will get back {final_amount,2} after {duration} years at the interest rate of {interest_rate}%")
    elif interest == "compound":
        final_amount = deposit*math.pow((1 + interest_rate/100),duration)
        print(f"You will get back {round(final_amount,2)} after {duration} years at the interest rate of {interest_rate}%")
        # round function has been used to round the final_amount to 2 decimals while printing
    else:
        print(f"\"{interest}\" is not a valid input")

elif choice == "bond":
    house_value = float(input("Enter the present value of the house : "))
    interest_rate = float(input("Enter the interest rate (as a percentage) : "))
    duration = float(input("Enter the number of months you plan to take to repay the bond :"))

    repayment = (interest_rate/(12*100) * house_value)/(1 - (1 + interest_rate/(12*100))**(-duration))

    print(f"You have to repay {round(repayment,2)} each month")
    # round function has been used to round the repayment to 2 decimals while printing

else:
    print(f"\"{choice}\" is not a valid input")