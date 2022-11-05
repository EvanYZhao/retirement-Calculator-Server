from flask import Flask, request, redirect
import numpy as np
import random
import statistics

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def myProfile(name, retirement_account_balance, yearly_expenses, years, stock_percentage):
    response_body = {
        "name": name,
        "retirement_account_balance": retirement_account_balance,
        "yearly_expenses": yearly_expenses,
        "years": years,
        "stock_percentage": stock_percentage
    }
    return response_body

@app.route("/retrieve", methods=['POST'])
def retrieveData():
    return null
    
    

@app.route("/user/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run()