# from a_int.models import CommissionTransactions , MainTransactions, BusinessTransactions, MainAccount, BusinessAccount, CommissionAccount, Business
# from a_int.payment.utils import balCalc, balCalc1

# # Transaction manager, manages all transactions.
# class TransactionManager:
#     def __init__(self, model, business_id=None, account=None, name=None, number=None, ref_code=None, item_id=None, amount=None, commission=None, credit=None, debit=None):
#         self.business_id = business_id
#         self.account = account
#         self.name = name
#         self.number = number
#         self.ref_code = ref_code
#         self.item_id = item_id
#         self.amount = amount
#         self.commission = commission
#         self.credit = credit
#         self.debit = debit
#         self.model = model

#     def __str__(self):
#         return f'{self.business_id},{self.name},{self.number},{self.ref_code}'
    
#     def __repr__(self):
#         return f'{self.business_id},{self.name},{self.number},{self.ref_code}'

#     def save(self):
#         if self.model.class_name() == 'MainTransactions':
#             main_transaction = MainTransactions.objects.create(
#                 business_id = self.business_id,
#                 account = self.account,
#                 name = self.name,
#                 number = self.number,
#                 ref_code = self.ref_code,
#                 item_id = self.item_id,
#                 amount =self.amount,
#                 commission = self.commission,
#                 debit = self.debit,
#                 credit = self.credit
#             )
#             main_transaction.save()
#             print(main_transaction)
#             am = AccountManager(main_transaction.transc_id, credit=self.credit, debit=self.debit)
#             am.updateDistribute(business_id=self.business_id, account=self.account, name=self.name, number=self.number, ref_code=self.ref_code, item_id=self.item_id, amount=self.amount, commission=self.commission, credit=self.credit, debit=self.debit)

#         elif self.model.class_name() == 'BusinessTransactions':
#             business_transaction = BusinessTransactions.objects.create(
#                 business_id = self.business_id,
#                 account = self.account,
#                 name = self.name,
#                 number = self.number,
#                 ref_code = self.ref_code,
#                 item_id = self.item_id,
#                 amount =self.amount,
#                 commission = self.commission,
#                 debit = self.debit,
#                 credit = self.credit
#             )
#             business_transaction.save()

#         elif self.model.class_name() == 'CommissionTransactions':
#             commission_transaction = CommissionTransactions.objects.create(
#                 business_id = self.business_id,
#                 account = self.account,
#                 commission = self.commission,
#                 debit = self.debit,
#                 credit = self.credit
#             )
#             commission_transaction.save()
#         else:
#             print(self.model.class_name())

# # Account Manager, manages account balances.
# class AccountManager:
#     def __init__(self, transc_id, credit=None, debit=None):
#         self.trans_id = transc_id
#         self.credit = credit
#         self.debit = debit
    
#     def updateDistribute(self, business_id=None, account=None, name=None, number=None, ref_code=None, item_id=None, amount=None, date=None, commission=None, credit=None, debit=None):
#         transc = MainTransactions.objects.get(transc_id=self.trans_id)
#         business = Business.objects.get(business_id=transc.business_id)
#         business_acc = business.account
#         commission, balance = balCalc(transc.commission, self.credit, business_acc.balance)
#         tm = TransactionManager(BusinessTransactions(), business_id=business.business_id, account=business_acc, name=name, number=number, ref_code=ref_code, item_id=item_id, amount=amount, commission=commission, credit=credit, debit=debit)
#         tm.save()
#         business_acc.balance = balance
#         business_acc.save()
#         transc.is_credited = True

#         business_acc1 = CommissionAccount.objects.get(account='8917360')
#         business_acc1.balance = balCalc1(commission, business_acc1.balance)
#         business_acc1.save()
#         tm1 = TransactionManager(CommissionTransactions(), account=business_acc1, business_id=business.business_id, commission=commission, credit=commission, debit=0)
#         tm1.save()
#         transc.is_success = True
#         transc.save()

# class Withdraw:
#     def __init__(self, ref_code=None, business_id=None, amount=None, credit=None, debit=None):
#         self.ref_code = ref_code
#         self.business_id = business_id
#         self.amount = amount
#         self.credit = credit
#         self.debit = debit

#     def save(self):
#         pass


# We write two classes
# 1. Transactions Manager
# 2. Accounts Manager
# For any successful payment, the transactions manager saves three transactions
from a_int.payment.utils import commCalc, calcBal

class TransactionsManager:
    '''
    Class Description
    '''
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def mainTransc(self):
        from a_int.models import MainTransactions, MainAccount
        account = MainAccount.objects.get(Name='Till')
        item_id = getattr(self, 'item_id', None)
        if item_id == 'A withdraw trasaction':
            fields  = ['business_id', 'ref_code', 'amount', 'item_id']
            transc_data = {field: getattr(self, field) for field in fields if hasattr(self, field)}
            debit = getattr(self, 'amount', None)
            more = {
                'account': account, 
                'credit': 0,
                'debit': debit
            }
            transc_data.update(more)
            main_transaction = MainTransactions(**transc_data)
            main_transaction.commission = None
            main_transaction.is_credited = None
            main_transaction.save()
            self.businessTransc(main_transaction)
            AccountManager.mainAccount(account, account.balance, 0, debit)
        else:
            fields  = ['business_id', 'ref_code', 'name', 'number', 'amount', 'item_id']
            transc_data = {field: getattr(self, field) for field in fields if hasattr(self, field)}
            credit = getattr(self, 'amount', None)
            more = {
                'account': account, 
                'credit': credit,
                'debit': 0
            }
            transc_data.update(more)
            main_transaction = MainTransactions(**transc_data)
            main_transaction.save()
            self.businessTransc(main_transaction)
            AccountManager.mainAccount(account, account.balance, credit, 0)


    def businessTransc(self, main_transaction):
        from a_int.models import BusinessTransactions, Business
        business_id = getattr(self, 'business_id', None)
        business = Business.objects.get(business_id=business_id)
        account = business.account
        item_id = getattr(self, 'item_id', None)
        if item_id == 'A withdraw trasaction':
            fields = ['business_id', 'ref_code', 'amount', 'item_id']
            transc_data = {field: getattr(self, field) for field in fields if hasattr(self, field)}
            debit = getattr(self, 'amount', None)
            more = {
                'account': account,
                'credit': 0,
                'debit': debit
            }
            transc_data.update(more)
            buss_transc = BusinessTransactions(**transc_data)
            buss_transc.save()
            main_transaction.is_credited = None
            main_transaction.is_success = True
            main_transaction.save()
            AccountManager.businessAccount(account, account.balance, 0, debit)
        else:
            fields = ['business_id', 'ref_code', 'name', 'number', 'amount', 'item_id']
            transc_data = {field: getattr(self, field) for field in fields if hasattr(self, field)}
            amount = getattr(self, 'amount', None)
            credit, comm = commCalc(amount, 0.02)
            more = {
                'account': account,
                'commission': comm,
                'credit': credit,
                'debit': comm
            }
            transc_data.update(more)
            buss_transc = BusinessTransactions(**transc_data)
            buss_transc.save()
            main_transaction.is_credited = True
            main_transaction.save()
            self.commTrasc(comm, main_transaction)
            AccountManager.businessAccount(account, account.balance, credit, comm)

    def commTrasc(self, comm, main_transaction):
        from a_int.models import CommissionTransactions, CommissionAccount
        fields = ['business_id',]
        transc_data = {field: getattr(self, field) for field in fields if hasattr(self, field)}
        account = CommissionAccount.objects.get(Name='Main')
        more = {
            'account': account,
            'commission': comm,
            'credit': comm,
            'debit': 0
        }
        transc_data.update(more)
        comm_trasc = CommissionTransactions(**transc_data)
        comm_trasc.save()

        main_transaction.is_success = True
        main_transaction.save()
        AccountManager.commAccount(account, account.balance, comm, 1)
        

class AccountManager:
    '''
    Class description
    '''
    def __init__(self):
        pass

    def mainAccount(account, bal, credit, debit):
        balance = calcBal(bal, credit, debit)
        account.balance = balance
        account.save()

    def businessAccount(account, bal, credit, debit):
        balance = calcBal(bal, credit, debit)
        account.balance = balance
        account.save()

    def commAccount(account, bal, credit, debit):
        balance = calcBal(bal, credit, debit)
        account.balance = balance
        account.save()