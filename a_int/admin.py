from django.contrib import admin
from .models import Business, Media, Product, Item, MainTransactions, BusinessTransactions, CommissionTransactions, BusinessAccount, MainAccount, CommissionAccount

admin.site.register(Business)
admin.site.register(Media)
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(MainAccount)
admin.site.register(BusinessAccount)
admin.site.register(CommissionAccount)
admin.site.register(MainTransactions)
admin.site.register(BusinessTransactions)
admin.site.register(CommissionTransactions)
# Register your models here.
