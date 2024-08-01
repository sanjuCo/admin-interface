# Utilities
# Calculates commision given percentage commision and credit
from decimal import Decimal, ROUND_HALF_UP
def commCalc(amount, commission):
    amount = Decimal(amount)
    commission = Decimal(commission)
    comm = amount*commission
    print(comm)
    credit = amount - comm
    print(credit)
    return credit, comm

def calcBal(bal, credit, debit):
    bal = Decimal(bal)
    credit = Decimal(credit)
    debit = Decimal(debit)
    balance = (bal + credit) - debit
    return balance