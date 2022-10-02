import main 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

for years in plot_years:
    # plot_years = str(plot_years)
    step1 = (1+(annual_return/compound_frequency))
    power_number2 = (compound_frequency * years)
    annual_return_divided = annual_return/compound_frequency
    half = (((step1**power_number2)-1)/annual_return_divided)
    future_and_deposits = regular_deposit * half 
    # print(futureanddeposits) # Debugging Tool 
    totalinvestmentover = Before_Future_Value + future_and_deposits  
    print(f"Year = {years} | {totalinvestmentover} \n")

