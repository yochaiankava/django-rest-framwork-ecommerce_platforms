from rest_framework import status
from django.shortcuts import render
from .models import *
from .serializers import *
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET', 'POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def products(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        maxprice = request.GET.get('maxprice')
        all_products = Product.objects.all()
        # search all product that name contains search parameter
        if search:
            all_products = all_products.filter(name__contains=search)
        # search all product that price <= maxprice (price__lte=maxprice)
        if maxprice:
            all_products = all_products.filter(price__lte=maxprice)

        all_products_json = ProductSerializer(all_products, many=True).data
        return Response(all_products_json)
    elif request.method == 'POST':
        # this line creates a serializer object from json data
        serializer = ProductSerializer(data=request.data)
        # this line checkes validity of json data
        if serializer.is_valid():
            # the serializer.save - saves a new product object
            serializer.save()
            # returns the object that was created including id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid. return errors.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    # get object from db by id
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        # create serializer from object
        serializer = ProductSerializer(product)
        # return json using serializer
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        # product.is_active = False
        # product.save()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view()
# def categories(request):
#     search = request.GET.get('search')
#     all_categories = Category.objects.all()
#     if search:
#         all_categories = all_categories.filter(name__contains=search)
#     all_categories_json = CategorySerializer(all_categories, many=True).data
#     return Response(all_categories_json)

@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        search = request.GET.get('search')
       
        all_categories = Category.objects.all()
        # search all product that name contains search parameter
        if search:
            all_categories = all_categories.filter(name__contains=search)        

        all_categories_json = CategorySerializer(all_categories, many=True).data
        return Response(all_categories_json)
    elif request.method == 'POST':
        # this line creates a serializer object from json data        
        serializer = CategorySerializer(data=request.data)
        # this line checkes validity of json data 
        if serializer.is_valid():
            # the serializer.save - saves a new product object
            serializer.save()
            # returns the object that was created including id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid. return errors.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):
    # get object from db by id
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        # create serializer from object
        serializer = CategorySerializer(category)
        # return json using serializer
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        # product.is_active = False
        # product.save()
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def cart(request):
    if request.method == 'GET':
        search = request.GET.get('search')
       
        all_carts = Cart.objects.all()
        # search all product that name contains search parameter
        if search:
            all_carts = all_carts.filter(name__contains=search)        

        all_carts_json = CartSerializer(all_carts, many=True).data
        return Response(all_carts_json)
    elif request.method == 'POST':
        # this line creates a serializer object from json data        
        serializer = CartSerializer(data=request.data)
        # this line checkes validity of json data 
        if serializer.is_valid():
            # the serializer.save - saves a new product object
            serializer.save()
            # returns the object that was created including id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid. return errors.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, id):
    # get object from db by id
    try:
        cart = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        # create serializer from object
        serializer = CartSerializer(cart)
        # return json using serializer
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        # product.is_active = False
        # product.save()
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    