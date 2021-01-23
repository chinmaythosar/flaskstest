import requests
import unittest

class Test:
    CreditCardNumber = '4111111111111111'
    CardHolder = 'abc'
    ExpirationDate = '06/22'
    SecurityCode= '011'
    Amount= '5'

    httpreq ='http://127.0.0.1:5000/?'

    def testall(self):
        requestString = self.httpreq + 'CreditCardNumber=' + self.CreditCardNumber + '&CardHolder=' + self.CardHolder + '&ExpirationDate=' + self.ExpirationDate + '&SecurityCode=' + self.SecurityCode + '&Amount=' + self.Amount
        r = requests.get(requestString)
        return r.status_code

    def testccn(self,ccn):
        requestString = self.httpreq + 'CreditCardNumber=' + ccn + '&CardHolder=' + self.CardHolder + '&ExpirationDate=' + self.ExpirationDate + '&SecurityCode=' + self.SecurityCode + '&Amount=' + self.Amount
        r = requests.get(requestString)
        return r.status_code

    def testccholder(self,ccholder):
        requestString = self.httpreq + 'CreditCardNumber=' + self.CreditCardNumber + '&CardHolder=' + ccholder+ '&ExpirationDate=' + self.ExpirationDate + '&SecurityCode=' + self.SecurityCode + '&Amount=' + self.Amount
        r = requests.get(requestString)
        return r.status_code

    def testexpdate(self,exp):
        requestString = self.httpreq + 'CreditCardNumber=' + self.CreditCardNumber + '&CardHolder=' + self.CardHolder + '&ExpirationDate=' + exp + '&SecurityCode=' + self.SecurityCode + '&Amount=' + self.Amount
        r = requests.get(requestString)
        return r.status_code


    def testcvv(self,cvv):
        requestString = self.httpreq + 'CreditCardNumber=' + self.CreditCardNumber + '&CardHolder=' + self.CardHolder + '&ExpirationDate=' + self.ExpirationDate + '&SecurityCode=' + cvv + '&Amount=' + self.Amount
        r = requests.get(requestString)
        return r.status_code   

    def testamt(self,amt):
        requestString = self.httpreq + 'CreditCardNumber=' + self.CreditCardNumber + '&CardHolder=' + self.CardHolder + '&ExpirationDate=' + self.ExpirationDate + '&SecurityCode=' + self.SecurityCode + '&Amount=' + amt
        r = requests.get(requestString)
        return r.status_code  

class TestStringMethods(unittest.TestCase):
    def test1(self):
        #Check if all okay
        new = Test()
        self.assertEqual(new.testall(),200)

    #Fail CreditCardNumber
    def test2(self):
        new = Test()
        #String
        self.assertEqual(new.testccn('abc'),400)
        #Less than 16 digits
        self.assertEqual(new.testccn('411111111111111'),400)
        #Invalid CC number
        self.assertEqual(new.testccn('4111111111111112'),400)
    
    #Fail Name
    def test3(self):
        new = Test()
        #Number
        self.assertEqual(new.testccholder('45'),400)
        #Invalid Chars
        self.assertEqual(new.testccholder('&]'),400)

    #Fail Expiry Date
    def test4(self):
        new = Test()
        #Old Date
        self.assertEqual(new.testexpdate('05/00'),400)
        #Invalid Date
        self.assertEqual(new.testexpdate('05/-01'),400)
        #String Date
        self.assertEqual(new.testexpdate('abc'),400)
        #Incomplete Date
        self.assertEqual(new.testexpdate('05'),400)

    #Fail CVV
    def test5(self):
        new = Test()
        #Short CVV
        self.assertEqual(new.testcvv('45'),400)
        #Short CVV
        self.assertEqual(new.testcvv('0'),400)
        #Short CVV Should fail if CVV is used in the API but not provided
        self.assertEqual(new.testcvv(''),400)
        #String CVV
        self.assertEqual(new.testcvv('a'),400)


    #Fail Amount
    def test6(self):
        new = Test()
        #Negative Amt
        self.assertEqual(new.testamt('-5'),400)
        #String Amt
        self.assertEqual(new.testamt('a'),400)


if __name__ == '__main__':
    unittest.main()