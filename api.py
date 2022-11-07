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
    return response_body

@app.route("/retrieve", methods=['POST'])
def retrieveData():
    request_data = request.get_json()
    app.logger.info(request_data)
    return request_data   

if __name__ == "__main__":
    app.run()