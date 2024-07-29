from a_int.models import CommissionTransactions , MainTransactions, BusinessTransactions, MainAccount, BusinessAccount, CommissionAccount, Business
from a_int.payment.utils import balCalc, balCalc1

# Transaction manager, manages all transactions.
class TransactionManager:
    def __init__(self, model, business_id=None, account=None, name=None, number=None, ref_code=None, item_id=None, amount=None, commission=None, credit=None, debit=None):
        self.business_id = business_id
        self.account = account
        self.name = name
        self.number = number
        self.ref_code = ref_code
        self.item_id = item_id
        self.amount = amount
        self.commission = commission
        self.credit = credit
        self.debit = debit
        self.model = model

    def __str__(self):
        return f'{self.business_id},{self.name},{self.number},{self.ref_code}'
    
    def __repr__(self):
        return f'{self.business_id},{self.name},{self.number},{self.ref_code}'

    def save(self):
        if self.model.class_name() == 'MainTransactions':
            main_transaction = MainTransactions.objects.create(
                business_id = self.business_id,
                account = self.account,
                name = self.name,
                number = self.number,
                ref_code = self.ref_code,
                item_id = self.item_id,
                amount =self.amount,
                commission = self.commission,
                debit = self.debit,
                credit = self.credit
            )
            main_transaction.save()
            print(main_transaction)
            am = AccountManager(main_transaction.transc_id, credit=self.credit, debit=self.debit)
            am.updateDistribute(business_id=self.business_id, account=self.account, name=self.name, number=self.number, ref_code=self.ref_code, item_id=self.item_id, amount=self.amount, commission=self.commission, credit=self.credit, debit=self.debit)

        elif self.model.class_name() == 'BusinessTransactions':
            business_transaction = BusinessTransactions.objects.create(
                business_id = self.business_id,
                account = self.account,
                name = self.name,
                number = self.number,
                ref_code = self.ref_code,
                item_id = self.item_id,
                amount =self.amount,
                commission = self.commission,
                debit = self.debit,
                credit = self.credit
            )
            business_transaction.save()

        elif self.model.class_name() == 'CommissionTransactions':
            commission_transaction = CommissionTransactions.objects.create(
                business_id = self.business_id,
                account = self.account,
                commission = self.commission,
                debit = self.debit,
                credit = self.credit
            )
            commission_transaction.save()
        else:
            print(self.model.class_name())

# Account Manager, manages account balances.
class AccountManager:
    def __init__(self, transc_id, credit=None, debit=None):
        self.trans_id = transc_id
        self.credit = credit
        self.debit = debit
    
    def updateDistribute(self, business_id=None, account=None, name=None, number=None, ref_code=None, item_id=None, amount=None, date=None, commission=None, credit=None, debit=None):
        transc = MainTransactions.objects.get(transc_id=self.trans_id)
        business = Business.objects.get(business_id=transc.business_id)
        business_acc = business.account
        commission, balance = balCalc(transc.commission, self.credit, business_acc.balance)
        tm = TransactionManager(BusinessTransactions(), business_id=business.business_id, account=business_acc, name=name, number=number, ref_code=ref_code, item_id=item_id, amount=amount, commission=commission, credit=credit, debit=debit)
        tm.save()
        business_acc.balance = balance
        business_acc.save()
        transc.is_credited = True

        business_acc1 = CommissionAccount.objects.get(account='8917360')
        business_acc1.balance = balCalc1(commission, business_acc1.balance)
        business_acc1.save()
        tm1 = TransactionManager(CommissionTransactions(), account=business_acc1, business_id=business.business_id, commission=commission, credit=commission, debit=0)
        tm1.save()
        transc.is_success = True
        transc.save()