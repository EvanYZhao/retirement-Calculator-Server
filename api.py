from flask import Flask, request, redirect
import numpy as np
import random
import statistics

app = Flask(__name__)

@app.route("/profile", methods = ['GET'])
def myProfile():
    response_body = {
        "name": "Evan",
        "retirement_account_balance": 1000000,
        "yearly_expenses": 75000,
        "years": 25,
        "stock_percentage": 50
    }
    # name, retirement_account_balance, yearly_expenses, years, stock_percentage
    return response_body

@app.route("/retrieve", methods=['POST'])
def retrieveData():
    request_data = request.get_json()
        
    firstName = request_data["firstName"]
    lastName = request_data["lastName"]
    app.logger.info(firstName)
    app.logger.info(lastName)
    return lastName

if __name__ == "__main__":
    app.run()