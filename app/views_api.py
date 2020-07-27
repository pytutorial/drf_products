from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

from .models import *
from .serializers import *
from .views_user import findProducts
from datetime import datetime

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

@api_view(['GET'])
def getProductDetail(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if product:
        data = ProductSerializer(product).data
        return Response({'product' : data})
    else:
        return Response({'error': 'Not found'})

@api_view(['POST'])
def orderProducts(request):
    try:
        customer = request.data.get('customer', {})
        items = request.data.get('items', [])

        order = Order()
        order.fullname = customer.get('fullname')
        order.phone = customer.get('phone')
        order.address = customer.get('address')
        order.orderDate = datetime.now()
        order.status = Order.Status.PENDING
        order.save()
        print(order)

        for item in items:
            orderline = Orderline()
            orderline.order = order
            orderline.product = Product(id=item.get('productId'))
            orderline.price = item.get('price')
            orderline.qty = item.get('qty')
            orderline.save()

        return Response({'success': True})
    except Exception as e:
        return Response({'success': False, 'error': str(e)})

