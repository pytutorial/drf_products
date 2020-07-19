from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

from .models import *
from .serializers import *
from .views_user import findProducts

@api_view(['GET'])
def searchProduct(request):
    #productList = Product.objects.all()
    productName = request.GET.get('product_name', '')
    categoryId = request.GET.get('category_id', '')
    categoryId = int(categoryId) if categoryId != '' else 0
    priceRange = request.GET.get('price_range', '')
    priceRange = int(priceRange) if priceRange != '' else 0
    
    productList = findProducts(productName, categoryId, priceRange)
    data = ProductSerializer(productList, many=True).data
    return Response({'productList': data})

@api_view(['GET'])
def getCategoryList(request):
    categoryList = Category.objects.all()    
    data = CategorySerializer(categoryList, many=True).data
    return Response({'categoryList': data})
