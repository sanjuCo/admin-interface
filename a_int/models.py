from django.contrib.auth.models import User
from django.db import models
import random
import string
import uuid
from .emails import credentials

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#account models
class MainAccount(models.Model):
    Name = models.CharField(max_length= 50)
    account = models.IntegerField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.Name}'
    
    def __repr__(self):
        return f'{self.Name}'

class MainTransactions(models.Model):
    transc_id = models.CharField(max_length=100, unique=True, editable=False)
    business_id = models.CharField(max_length=200)
    account = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True)
    number = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    item_id = models.CharField(max_length=1000000, null=True)
    date = models.DateTimeField(auto_now_add=True)
    commission = models.DecimalField(max_digits=8, decimal_places=2, default=2, null=True)
    credit = models.DecimalField(max_digits=8, decimal_places=2)
    debit = models.DecimalField(max_digits=8, decimal_places=2)
    is_credited = models.BooleanField(default=False, null=True)
    is_success = models.BooleanField(default=False, null=True)

    def class_name(self):
        return '%s' % self.__class__.__name__
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.transc_id:
                self.transc_id = str(uuid.uuid4())
        super(MainTransactions, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.transc_id}'
    
    def __repr__(self):
        return f'{self.transc_id}'

class BusinessAccount(models.Model):
    Name = models.CharField(max_length= 50)
    account = models.IntegerField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.Name}'
    
    def __repr__(self):
        return f'{self.Name}'

class BusinessTransactions(models.Model):
    transc_id = models.CharField(max_length=100, unique=True, editable=False)
    business_id = models.CharField(max_length=200)
    account = models.ForeignKey(BusinessAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    number = models.IntegerField(null=True)
    ref_code = models.CharField(max_length=50)
    item_id = models.CharField(max_length=1000000)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=2)
    date = models.DateTimeField(auto_now_add=True)
    commission = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    credit = models.DecimalField(max_digits=8, decimal_places=2)
    debit = models.DecimalField(max_digits=8, decimal_places=2)

    def class_name(self):
        return '%s' % self.__class__.__name__
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.transc_id:
                self.transc_id = str(uuid.uuid4())
        super(BusinessTransactions, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.business_id}'
    
    def __repr__(self):
        return f'{self.business_id}'

class CommissionAccount(models.Model):
    Name = models.CharField(max_length= 50)
    account = models.IntegerField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.Name}'
    
    def __repr__(self):
        return f'{self.Name}'

class CommissionTransactions(models.Model):
    transc_id = models.CharField(max_length=100, unique=True, editable=False)
    business_id = models.CharField(max_length=200)
    account = models.ForeignKey(CommissionAccount, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    commission = models.DecimalField(max_digits=8, decimal_places=2, default=2)
    credit = models.DecimalField(max_digits=8, decimal_places=2)
    debit = models.DecimalField(max_digits=8, decimal_places=2)

    def class_name(self):
        return '%s' % self.__class__.__name__
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.transc_id:
                self.transc_id = str(uuid.uuid4())
        super(CommissionTransactions, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.business_id}'
    
    def __repr__(self):
        return f'{self.business_id}'
    
    
class Business(models.Model):
    business_id = models.CharField(max_length=200, editable=False)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='image/')
    email = models.EmailField(max_length=200, verbose_name='Business Email', unique=True)
    phone = models.CharField(max_length=13)
    account = models.OneToOneField(BusinessAccount, on_delete=models.CASCADE, related_name='business_account', null=True)
    administrator = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administered_business', editable=False)

    def __str__(self):
        return f"{self.name}" 
    
    def __repr__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new instance
            if not self.business_id:
                self.business_id = str(uuid.uuid4()) + str(random.randint(130, 999))
            username = self.name                                                                                                                                                                                                                                                                     
            password = generate_password()
            user = User.objects.create_user(username=username, password=password)
            user.save()
            self.administrator = user
            credentials(username, password, self.email, 'https://pollstats.co.ke')
        super(Business, self).save(*args, **kwargs)
    

class Product(models.Model):
    product_id = models.CharField(max_length=200, unique=True, editable=False)
    name = models.CharField(max_length=70)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.product_id:
                self.product_id = self.business.business_id +  str(uuid.uuid4())
        super(Product, self).save(*args, **kwargs)
    
class Item(models.Model):
    item_id = models.CharField(max_length=200, unique=True, editable=False)
    name = models.CharField(max_length=70)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    f1 = models.FileField(upload_to='items/%Y/%M')
    f2 = models.FileField(upload_to='items/%Y/%M')
    f3 = models.FileField(upload_to='items/%Y/%M')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    color = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.item_id:
                self.item_id = self.product.product_id +  str(uuid.uuid4())
        super(Item, self).save(*args, **kwargs)

# Extra Images Modal
class Media(models.Model):
    name = models.CharField(max_length=10, verbose_name='name')
    image = models.ImageField(upload_to='images/')

    class Meta:
        unique_together = ['name']
        verbose_name = 'Media'

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
    