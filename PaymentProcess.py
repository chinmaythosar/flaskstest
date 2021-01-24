

class PaymentProcess:

    def Processing(self,amount):
        if(amount < 20):
            return self.PremiumPaymentGateway()

        elif(amount > 20 and amount <= 500 ):
            if (self.ExpensivePaymentGateway() == False):
                return self.CheapPaymentGateway()
            else:
                return True
        else:
            success = False
            x = 0
            while (success == False and x < 3):
                success = self.ExpensivePaymentGateway()
                x = x+1
            return success
    def PremiumPaymentGateway(self):
        return True
    
    def ExpensivePaymentGateway(self):
        return True

    def CheapPaymentGateway(self):
        return True