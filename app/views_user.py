#views_user.py
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *
from datetime import datetime

def findProducts(productName, categoryId, priceRange):
    prices = {
        0:{'min':None, 'max':None},
        1:{'min':None, 'max':10},
        2:{'min':10,   'max': 15},
        3:{'min':15,   'max': 20},
        4:{'min':20,   'max': None},
    }
    minPrice, maxPrice = prices[priceRange]['min'], prices[priceRange]['max']
    productList = Product.objects.all()
    if productName != '':
        productList = productList.filter(name__contains=productName)
    if minPrice != None:
        productList = productList.filter(price__gte=minPrice*1e6)
    if maxPrice:
        productList = productList.filter(price__lte=maxPrice*1e6)
    if categoryId:
        productList = productList.filter(category__id=categoryId)
    return productList

def index(request):
    productName = request.GET.get('product_name', '')
    categoryId = request.GET.get('category_id', '')
    categoryId = int(categoryId) if categoryId != '' else 0
    priceRange = request.GET.get('price_range', '')
    priceRange = int(priceRange) if priceRange != '' else 0

    productList = findProducts(productName, categoryId, priceRange)
    categoryList = Category.objects.all()
    context = {
        'categoryList': categoryList,
        'productList': productList,
        'productName': productName,
        'categoryId': categoryId,
        'priceRange': priceRange
    }
    return render(request, 'user/index.html',
                    context)

def viewProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'user/product.html', context)       

def purchase(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = PurchaseForm()
   
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            request.session['purchase_form'] = form.cleaned_data
            return redirect('purchase-confirm', pk)

    context = {'product' : product, 'form': form}
    return render(request, 'user/purchase.html', context)                 

def purchaseConfirm(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':        
        purchase_form = request.session['purchase_form']
        order = Order()
        order.fullname = purchase_form['fullname']
        order.phone = purchase_form['phone']
        order.address = purchase_form['address']
        order.product = product
        order.orderDate = datetime.now()
        order.status = Order.Status.PENDING
        order.save()
        return redirect('thank-you')
    context = {'product': product}
    return render(request, 'user/purchase_confirm.html', context)    

def thankYou(request):
    return render(request, 'user/thank_you.html')    