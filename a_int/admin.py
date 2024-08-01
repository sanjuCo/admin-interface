from django.contrib import admin
from .models import Business, Media, Product, Item, MainTransactions, BusinessTransactions, CommissionTransactions, BusinessAccount, MainAccount, CommissionAccount

admin.site.register(Business)
admin.site.register(Media)
admin.site.register(Product)
admin.site.register(Item)
class MainAccountAdmin(admin.ModelAdmin):
    list_display = ['Name', 'account', 'balance']

class BusinessAccountAdmin(admin.ModelAdmin):
    list_display = ['Name', 'account', 'balance']

class CommissionAccountAdmin(admin.ModelAdmin):
    list_display = ['Name', 'account', 'balance']

class MainTransactionsAdmin(admin.ModelAdmin):
    list_display = ['date', 'transc_id', 'business_id', 'amount', 'f_commission', 'f_credit', 'f_debit', 'is_credited', 'is_success']

    def f_commission(self, obj):
        return f'{obj.commission}%'
    f_commission.short_description = 'commission'

    def f_credit(self, obj):
        return f'+{obj.credit}' if obj.credit != 0 else obj.credit
    f_credit.short_description = 'credit'
    
    def f_debit(self, obj):
        return f'-{obj.debit}' if obj.debit != 0 else obj.debit
    f_debit.short_description = 'debit'

class BusinessTransactionsAdmin(admin.ModelAdmin):
    list_display = ['date', 'transc_id', 'amount', 'commission', 'f_credit', 'f_debit']

    def f_credit(self, obj):
        return f'+{obj.credit}' if obj.credit != 0 else obj.credit
    f_credit.short_description = 'credit'
    
    def f_debit(self, obj):
        return f'-{obj.debit}' if obj.debit != 0 else obj.debit
    f_debit.short_description = 'debit'

class CommissionTransactionsAdmin(admin.ModelAdmin):
    list_display = ['date', 'transc_id', 'business_id', 'commission', 'f_credit', 'f_debit']

    def f_credit(self, obj):
        return f'+{obj.credit}' if obj.credit != 0 else obj.credit
    f_credit.short_description = 'credit'
    
    def f_debit(self, obj):
        return f'-{obj.debit}' if obj.debit != 0 else obj.debit
    f_debit.short_description = 'debit'

# Registering the admin classes
admin.site.register(MainAccount, MainAccountAdmin)
admin.site.register(BusinessAccount, BusinessAccountAdmin)
admin.site.register(CommissionAccount, CommissionAccountAdmin)

admin.site.register(MainTransactions, MainTransactionsAdmin)
admin.site.register(BusinessTransactions, BusinessTransactionsAdmin)
admin.site.register(CommissionTransactions, CommissionTransactionsAdmin)

# Register your models here.
