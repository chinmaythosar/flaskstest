import flask
from flask import request, jsonify
from CreditCardChecker import CreditCardChecker
from datetime import datetime
import re

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def ProcessPayment():
    #All are true unless error since some can be missing
    ccnstatus = True
    ccholder = True
    ccdate = True
    cvv = True
    amt = True
    #Check CC validity use Lahms Algorithm
    if 'CreditCardNumber' in request.args:
        ccn = request.args['CreditCardNumber']
        ccnstatus = CreditCardChecker(ccn).valid()
    else:
        ccnstatus = False

    #Check if card holder is a valid string (no length limit specified)
    if 'CardHolder' in request.args:
        cch = request.args['CardHolder']
        cch = cch.replace(' ', '')
        if len(cch)>0:
            re1 = re.compile(r"[<>/{}[\]~`]")
            if re1.search(cch):
                ccholder = False

            re2 = re.compile(r"[1234567890-]")
            if re2.search(cch):
                ccholder = False
        else:
            ccholder = False

    else:
        cch = False
    #Check if expiration date is greater than today
    if 'ExpirationDate' in request.args:
        expdate = request.args['ExpirationDate']

        tempdate = expdate.split('/')
        if len(tempdate) is not 2:
            ccdate = False
        
        todaymonth = datetime.now().month
        todayyear = datetime.now().year

        todayyear = todayyear - 2000
        
        checkyear = 0
        checkmonth = 0
        if ccdate:
            try:
                checkmonth = int(tempdate[0])
            except ValueError:
                ccdate = False
            try:
                checkyear = int(tempdate[1])
            except ValueError:
                ccdate = False

            if(checkmonth<todaymonth):
                ccdate = False
            if(checkyear<todayyear):
                ccdate = False
    else:
        ccdate = False
    #Check if security code is a valid code if it exists
    if 'SecurityCode' in request.args:
        cvvcode = request.args['SecurityCode']

        try:
            int(cvvcode)
            cvvlength = len(cvvcode)
            if cvvlength is 3 and int(cvvcode) > 0:
                cvv = True
            else:
                cvv = False
        except ValueError:
            cvv = False


    #Check if amount is positive
    if 'Amount' in request.args:
        amountval = request.args['Amount']
        try:
            int(amountval)
            if(int(amountval)>0):
                amt = True
            else:
                amt = False
        except ValueError:
            amt = False

    else:
        amt = False
    # Check if any inconsistencies before hitting paymentgateway

    if amt and cvv and ccdate and ccnstatus and ccholder:
        return 'ok!', 200
    else:
        return 'bad request!', 400
    
app.run()
