from django.shortcuts import render, redirect
from .models import Media, Business, Product, Item, MainAccount, MainTransactions
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProdForm, ItemForm
from a_int.payment.core import TransactionsManager
from django.http import HttpResponse

@login_required
def dashboard(request):
    admin = request.user
    if admin.is_authenticated:
        business = Business.objects.get(administrator=admin)
        
    context = {
        'admin': admin,
        'business': business
    }
    return render(request, 'dashboard.html', context)

@login_required
def items(request):
    admin = request.user
    if admin.is_authenticated:
        business = Business.objects.get(administrator=admin)
    prod_form = ProdForm()
    item_form = ItemForm()
    products = Product.objects.filter(business=business)
    items = Item.objects.filter(product__business__administrator=admin)
    context = {
        'items': items,
        'products': products,
        'admin': admin,
        'business': business,
        'prod_form': prod_form,
        'item_form': item_form
    }
    return render(request, 'items.html', context)

def addProd(request):
    if request.method == 'POST':
        prod_form = ProdForm(request.POST)
        admin = request.user
        if admin.is_authenticated:
            business = Business.objects.get(administrator=admin)
            if prod_form.is_valid():
                product = prod_form.save(commit=False)
                product.business = business
                product.save()
                return redirect('items')

def delProd(request):
    print(request.POST)
    if request.method == 'POST':
        prod_ids = request.POST.getlist('products')
        print(prod_ids)
        for id in prod_ids:
            product = Product.objects.get(product_id=id)
            product.delete()
        return redirect('items')

def addItem(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES, user=request.user)
        print(request.FILES)
        if item_form.is_valid():
            item_form.save()
            return redirect('items')
        else:
            print(item_form.errors)
    else:
        item_form = ItemForm(user=request.user) 

def delItem(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('items')
        for id in item_ids:
            item = Item.objects.get(item_id=id)
            item.delete()
        return redirect('items')

@login_required
def transactions(request):
    return render(request, 'transactions.html',)

@login_required
def stats(request):
    return render(request, 'stats.html')

@login_required
def documentation(request):
    return render(request, 'd_base.html')

# Login Logic
def login_user(request):
    suite = Media.objects.get(name='suite')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'image': suite})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

def test(request):
    business = Business.objects.get(name='Liquor')
    tm = TransactionsManager(business_id=business.business_id, ref_code='nuufbuf', name='Samuel', number=254757077058, amount=1520, item_id='ufdhufdbdf')
    tm.mainTransc()
    return HttpResponse('Done')

def test1(request):
    business = Business.objects.get(name='Liquor')
    tm = TransactionsManager(business_id=business.business_id, ref_code='hufhufb', amount='2012', item_id='A withdraw trasaction')
    tm.mainTransc()
    return HttpResponse('Withdraw successfull')