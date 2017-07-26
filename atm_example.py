import time
import random

#Tray in ATM machine {<currency denomincation> : <number of notes>}
atm_tray = {50:50, 100:100, 500:500, 1000:1}


class Atm:
    '''Atm example - just to understand how ATM note calculation works
    '''
    def __init__(self, amount):
        self.amount = amount

    def calculate_amt_available(self):
        total_cash = 0
        for denomination, number_of_notes in atm_tray.iteritems():
            total_cash = denomination * number_of_notes
            
        if total_cash > self.amount:
            print "Sufficient currency is there in the ATM"
        else:
            print "Enter lower amount"


    def calculate_denominations(self):
        amount = self.amount
        denom = {}
        for denomination in sorted(atm_tray.keys(), reverse=True):
            if amount == 0:
                break
            num, reminder = divmod(amount, denomination)
            if num > 0 and atm_tray[denomination] >= num:                
                denom[denomination] = num
                amount = amount - (denomination * num)
        print denom
                
            
    def calculate_denomination_availability(self):
        if self.amount % min(atm_tray.keys()) == 0:
            self.calculate_denominations()            
            print "Available"
        else:
            print "No denominations"
        


if __name__ == '__main__':
    tx = Atm(2850)
    tx.calculate_amt_available()
    tx.calculate_denomination_availability()
