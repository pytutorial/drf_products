from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                    password=request.POST['password1'])
            login(request, user)
            return redirect('list-category')
    return render(request, 'registration/signup.html',
                     {'form':form})
#http://localhost:8000/list_category
@login_required
def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'staff/category/list.html', {'categoryList': categoryList})

@login_required
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    return render(request, 'staff/category/form.html', {'form': form})

@login_required
def editCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    return render(request, 'staff/category/form.html', {'form': form})

@login_required
def deleteCategory(request, pk):    
    category = get_object_or_404(Category,pk=pk) 
    category.delete()
    return redirect('list-category')

@login_required
def listProduct(request):
    productList = Product.objects.all()
    return render(request, 'staff/product/list.html', {'productList': productList})

@login_required
def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'staff/product/form.html', {'form': form})

@login_required
def editProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'staff/product/form.html', {'form': form})

@login_required
def deleteProduct(request, pk):    
    product = get_object_or_404(Product,pk=pk) 
    product.delete()
    return redirect('list-product')    