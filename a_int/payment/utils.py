# Utilities
# Calculates commision given percentage commision and credit
def balCalc(comm, credit, bal):
    comm = (credit*comm)/100
    bal = credit-comm
    return comm, bal

def balCalc1(credit, bal):
    bal = bal + credit
    return bal