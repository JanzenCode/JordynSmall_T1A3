import src.help as help 

#Investment Calculator for Individuals Making Inital and Monthly Contributions:
# CollectUsersName/Deposit/RegularAmounts/Time/Frequency/TotalYears/ExpectedReturn

InvestorName = input("Welcome to the Long-Term Investment Calculator, please enter your name: ") 
Start = input(f"Hello {InvestorName}, would you like to calculate your investment potential? (y/n): ")

if Start == "n": 
    print("You can try again anytime.")
    exit()

elif Start == "y":

    inital_deposit = input(f"{InvestorName}, please enter your inital deposit as a whole number such as 10000: ")
    regular_deposit = input(f"{InvestorName}, please enter your regular deposit as a whole number such as 100: ")
    deposit_frequency = input(f"{InvestorName}, please enter how many times you wish to deposit: for example, 4 = 4 times per month: ")
    compound_frequency = print(f"{InvestorName}, your investment will compound monthly.")
    num_of_years = input(f"{InvestorName}, please enter the desired amount of years you'd like to invest for: ")
    annual_return = input(f"{InvestorName}, please enter the desired return per year you expect; for example, 5 8 or 11: ")
    set_years_1 = int(30)
    set_years_2 = int(50)
    set_years_3 = int(70)

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

    # print(f"Here: {BeforeFutureValue}") # Debugging Tool 

    # Calculating the Future Value of The Investment 

    step1 = (1+(annual_return/compound_frequency))
    powernumber2 = (compound_frequency * num_of_years)
    annualreturndivided = annual_return/compound_frequency

    half = (((step1**powernumber2)-1)/annualreturndivided)
    futureanddeposits = regular_deposit * half 
    # print(futureanddeposits) # Debugging Tool 

    totalinvestmentovertime = BeforeFutureValue + futureanddeposits
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{InvestorName}, This is the potential return on your investment based on your inital deposit and monthly contributions: {totalinvestmentovertime}")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    
    # Investment Information + Set Number of Years & Rates


    step1 = (1+(annual_return/compound_frequency))
    powernumber2 = (compound_frequency * set_years_1)
    annualreturndivided = annual_return/compound_frequency

    half = (((step1**powernumber2)-1)/annualreturndivided)
    futureanddeposits = regular_deposit * half 
    # print(futureanddeposits) # Debugging Tool 

    totalinvestmentover30 = BeforeFutureValue + futureanddeposits

    print(f"Investment after 30 years: {totalinvestmentover30}")

# ------------------------------------------------------------------------------------------------

    step1 = (1+(annual_return/compound_frequency))
    powernumber2 = (compound_frequency * set_years_2)
    annualreturndivided = annual_return/compound_frequency

    half = (((step1**powernumber2)-1)/annualreturndivided)
    futureanddeposits = regular_deposit * half 
    # print(futureanddeposits) # Debugging Tool 

    totalinvestmentover50 = BeforeFutureValue + futureanddeposits
  
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Investment after 50 years: {totalinvestmentover50}")

# ------------------------------------------------------------------------------------------------
    step1 = (1+(annual_return/compound_frequency))
    powernumber2 = (compound_frequency * set_years_3)
    annualreturndivided = annual_return/compound_frequency

    half = (((step1**powernumber2)-1)/annualreturndivided)
    futureanddeposits = regular_deposit * half 
    # print(futureanddeposits) # Debugging Tool 

    totalinvestmentover70 = BeforeFutureValue + futureanddeposits

    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Investment after 70 years: {totalinvestmentover70}")