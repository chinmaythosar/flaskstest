import flask
from flask import request, jsonify
from CreditCardChecker import CreditCardChecker
from datetime import datetime
import re
from TestValidity import ValidityClass
from PaymentProcess import PaymentProcess

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def ProcessPayment():
    valid = False

    newObj = ValidityClass()

    valid = newObj.TestValid(request)

    if valid:
        #Run payment Processing
        amount = request.args['Amount']
        amount = int(amount)
        processObj = PaymentProcess()

        status = processObj.Processing(amount)

        if(status == True):
            return 'ok!', 200
        else:
            return 'internal server error!', 500
    else:
        return 'bad request!', 400
    
app.run()
