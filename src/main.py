import help
import matplotlib.pyplot as plt 
import numpy as np
#Investment Calculator for Individuals Making Inital and Monthly Contributions:
# CollectUsersName/Deposit/RegularAmounts/Time/Frequency/TotalYears/ExpectedReturn
def calculator():
    from calendar import month
    import datetime
    begin = True
    completion = False
    Investor_Name = input("Welcome to the Long-Term Investment Calculator, please enter your name: ")
    while begin:
        if completion == False:
            Start = input(f"Hello {Investor_Name}, would you like to calculate your investment potential? (y/n): ")
        elif completion == True:
            Start = input(f"Hello {Investor_Name}, would you like to calculate other investment potential using different numbers? (y/n): ")
        if Start == "y":
            inital_deposit = input(f"{Investor_Name}, please enter your inital deposit as a whole number such as 10000: ")
            regular_deposit = input(f"{Investor_Name}, please enter your regular deposit as a whole number such as 100: ")
            deposit_frequency = input(f"{Investor_Name}, please enter how many times you wish to deposit: for example, 4 = 4 times per month: ")
            compound_frequency = print(f"{Investor_Name}, your investment will compound monthly.")
            num_of_years = input(f"{Investor_Name}, please enter the desired amount of years you'd like to invest for: ")
            annual_return = input(f"{Investor_Name}, please enter the desired return per year you expect; for example, 5 8 or 11: ")
            set_years = [30, 50, 70]
            plot_years = [10, 20, 30, 40, 50, 60, 80, 90]
            time = datetime.datetime.now()
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
            power_number = (compound_frequency * num_of_years)
            Before_Future_Value = inital_deposit * (preliminary ** power_number)
            # print(f"Here: {BeforeFutureValue}") # Debugging Tool 
            # Calculating the Future Value of The Investment 
            step1 = (1+(annual_return/compound_frequency))
            power_number2 = (compound_frequency * num_of_years)
            annual_return_divided = annual_return/compound_frequency
            half = (((step1**power_number2)-1)/annual_return_divided)
            future_and_deposits = regular_deposit * half 
            # print(futureanddeposits) # Debugging Tool 
            total_investment_over_time = Before_Future_Value + future_and_deposits
            # on this day (year month day) your investment will be x amount 
            print("--------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"{Investor_Name}, This is the potential return on your investment in {time.year + num_of_years} based on your inital deposit and monthly contributions will be: {total_investment_over_time}")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------")
            # Investment Information + Set Number of Years & Rates
            for years in set_years:
                step1 = (1+(annual_return/compound_frequency))
                power_number2 = (compound_frequency * years)
                annual_return_divided = annual_return/compound_frequency
                half = (((step1**power_number2)-1)/annual_return_divided)
                future_and_deposits = regular_deposit * half 
                # print(futureanddeposits) # Debugging Tool 
                totalinvestmentover = Before_Future_Value + future_and_deposits
                print(f"Investment after ({years} years) or in {time.year + years} will be {totalinvestmentover} \n")
            # Debugged Information 
            years_list = []
            totalinvestment_list = []
            for years in plot_years:
                # plot_years = str(plot_years)
                years_list.append(years)
                step1 = (1+(annual_return/compound_frequency))
                power_number2 = (compound_frequency * years)
                annual_return_divided = annual_return/compound_frequency
                half = (((step1**power_number2)-1)/annual_return_divided)
                future_and_deposits = regular_deposit * half 
                # print(futureanddeposits) # Debugging Tool 
                totalinvestmentoverre = Before_Future_Value + future_and_deposits  
                totalinvestment_list.append(totalinvestmentoverre)
                # print(f"Year = {years} | {totalinvestmentoverre} \n") For Debugging
            completion = True
            plt.axes(ylabel = "Investment $", xlabel = "No. Of Years", title = Investor_Name + ", Your Investment Return Graphically Represented Over Time")
            plt.plot(years_list, totalinvestment_list)
            plt.show()
        else:
            print("You can try again anytime.")
            begin = False
calculator()
