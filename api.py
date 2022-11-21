from flask import Flask, request, redirect, session, url_for
import numpy as np
import random
import statistics

api = Flask(__name__)
# application.secret_key = "super_secret_key"

# ### PROCESSING ###
# # Loading in stock, bond, and inflation rates in US from years 1980-2021
# historical_stock_returns = np.loadtxt("./data/SnP500_stockReturns.txt", delimiter=',')
# historical_bond_returns = np.loadtxt("./data/BloombergAgg_bondReturns.txt", delimiter=',')
# historical_inflation_rates = np.loadtxt("./data/inflationRate.txt", delimiter=',')

# # Functions defined to randomly choose among the 42 rates in each loaded-in txt file
# def ChangeInBalanceStocks(initial_balance):
#     rate = random.choice(historical_stock_returns)
#     return initial_balance*rate

# def ChangeInBalanceBonds(initial_balance):
#     rate = random.choice(historical_bond_returns)
#     return initial_balance*rate

# def Inflation():
#     return random.choice(historical_inflation_rates)

# # Returns rate of change for all 3 fluctuating factors in a single tuple
# def YearData():
#     year = random.randrange(0,41)
#     return (historical_stock_returns[year], historical_bond_returns[year], historical_inflation_rates[year])

# def retirementCalculator(retirement_account_balance, yearly_expenses, years, stock_percentage):
#     # Edge cases where inputs are unreasonable (return 0s for results):
#     # 1. yearly expenses > projected retirement balance
#     # 2. yearly expenses == projected retirement balance but years > 1
#     if (retirement_account_balance < yearly_expenses) or ((retirement_account_balance == yearly_expenses) and years > 1) :
#         return{
#             "retirement_account_balance": session.get('retirement_account_balance'),
#             "yearly_expenses": session.get('yearly_expenses'),
#             "years": session.get('years'),
#             "stock_percentage": session.get('stock_percentage'),
#             "percent_successful": 0,
#             "final_balance_average": 0,
#             "final_balance_stdev": 0
#         }
        
#     final_balances = []
#     ran_out = 0
#     # Beginning of simulation
#     for i in range(10000):
#         # Initial Conditions
#         time = 0
#         balance_stocks = retirement_account_balance * stock_percentage
#         balance_bonds = retirement_account_balance * (1.0 - stock_percentage)
#         expenses = yearly_expenses
                
#         while (time < years):
#             time += 1
#             # Increase balance and time
#             stock_perform, bond_perform, inflation = YearData()
#             balance_stocks *= (1.0 + stock_perform)
#             balance_bonds *= (1.0 + bond_perform)
                    
#             # Rebalance account based on originally chosen percentage for stock investment
#             balance_mixed = balance_stocks + balance_bonds
#             target_stocks = balance_mixed * stock_percentage
#             amount_to_move = balance_stocks - target_stocks
#             balance_stocks -= amount_to_move
#             balance_bonds += amount_to_move
                    
#             # Remove this years expenses which change with inflation
#             expenses *= (1.0 + inflation)
#             balance_stocks -= expenses * stock_percentage
#             balance_bonds -= expenses * (1.0 - stock_percentage)
                    
#             if (balance_stocks < 0):
#                 # Ran out of money. Increase ran_out count and set time to years to stop loop
#                 ran_out += 1
#                 time = years
                    
#         if (balance_stocks > 0):
#             # Money lasted all the way - save the final balance info
#             final_balances.append(balance_stocks + balance_bonds)

#     # Final Data analysis
#     percent_successful = (10000 - ran_out)/10000 * 100
#     final_balance_average = statistics.mean(final_balances)
#     final_balance_standard_deviation = statistics.stdev(final_balances)
    
#     return {
#         "retirement_account_balance": session.get('retirement_account_balance'),
#         "yearly_expenses": session.get('yearly_expenses'),
#         "years": session.get('years'),
#         "stock_percentage": session.get('stock_percentage'),
#         "percent_successful": round(percent_successful,2),
#         "final_balance_average": round(final_balance_average,2),
#         "final_balance_stdev": round(final_balance_standard_deviation,2)
#     }
    
### VIEWS ###
# Homepage that user sees if they navigate to homepage of API
@api.route("/")
def homePage():
    return "Hey, You're not supposed to be here! Go check out the actual website instead!"

# # Sends data to React to display user's retirement predictions
# @application.route("/results", methods = ['GET'])
# def results():
#     if session.get('retirement_account_balance'):
#         balance = session.get('retirement_account_balance')
#         expenses = session.get('yearly_expenses')
#         years = session.get('years')
#         stock = session.get('stock_percentage')
#         return retirementCalculator(balance, expenses, years, stock)
#     else:
#         return  {
#         "percent_successful": 0,
#         "final_balance_average": 0,
#         "final_balance_stdev": 0
#     }

# # Takes data from form, stores them into session keys and redirects to /results view to do computation right away
# @application.route("/retrieve", methods=['POST'])
# def retrieveData():
#     request_data = request.get_json()
#     session["retirement_account_balance"] = float(request_data['retirement_account_balance'])
#     session["yearly_expenses"] = float(request_data['yearly_expenses'])
#     session["years"] = float(request_data['years'])
#     session["stock_percentage"] = (float(request_data['stock_percentage'])/100)
#     return redirect(url_for('results')) 

# # Clears the session with each page refresh and after every get request made to the /retrieve view
# @application.route("/refresh")
# def refresh():
#     session.clear()
#     return "Refresh complete!"

# # if __name__ == "__main__":
# #     app.run()