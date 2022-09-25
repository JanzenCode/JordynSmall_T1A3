# StartOfProgram
# InvestorName = str
# inital_deposit = int # Program will use deposits as whole numbers not floats. 
# regular_deposit = int 
# deposit_frequency = int 
# compound_frequency = 1/12
# num_of_years = int
# annual_return = float 

# CollectUsersName/Deposit/RegularAmounts/Time/Frequency/TotalYears/ExpectedReturn

InvestorName = input("Welcome to the Long-Term Investment Calculator, please enter your name: ") 
input(f"Hello {InvestorName}, would you like to calculate your investment potential? (y/n) ")
if "y":

    inital_deposit = input(f"{InvestorName}, please enter your inital deposit as a whole number such as 10000: ")
    regular_deposit = input(f"{InvestorName}, please enter your regular deposit as a whole number such as 100: ")
    deposit_frequency = input(f"{InvestorName}, please enter how many times you wish to deposit: for example, 4 = 4 times per month: ")
    compound_frequency = print(f"{InvestorName}, your investment will compound monthly.")
    num_of_years = input(f"{InvestorName}, please enter the desired amount of years you'd like to invest for: ")
    annual_return = input(f"{InvestorName}, please enter the desired return per year you expect; for example, 5 8 or 11: ")

    # print(inital_deposit * 1 + (annual_return/compound_frequency) ** num_of_years)

# Convert InputStrings into Integers

inital_deposit = int(inital_deposit)
regular_deposit = int(regular_deposit)
deposit_frequency = int(deposit_frequency)
compound_frequency = int(12)
num_of_years = int(num_of_years)
annual_return = (int(annual_return))/100

# Calculating the Compound Interest Earned over the Investment Period

preliminary = (1+(annual_return/compound_frequency))
powernumber = (compound_frequency * num_of_years)

BeforeFutureValue = inital_deposit * (preliminary ** powernumber)
print(f"Here: {BeforeFutureValue}") # Debugging Tool 





