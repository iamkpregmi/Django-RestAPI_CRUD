from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def product(request):
    products_obj = products.objects.all()
    serializers = productsSerializer(products_obj, many=True)
    return Response({'Products': serializers.data})


@api_view(['GET'])
def single_product(request,id):
    products_obj = products.objects.get(id=id)
    serializers = productsSerializer(products_obj)
    return Response({'Products': serializers.data})


@api_view(['POST'])
def add_product(request):
    data = request.data
    serializers = productsSerializer(data=request.data)

    if not serializers.is_valid():
        return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
    else:
        serializers.save()
    return Response({'Products': serializers.data, 'message': 'Your data is saved successfully'})


@api_view(['PATCH'])
def edit_product(request,id):
    try:
        products_obj = products.objects.get(id=id)

        serializers = productsSerializer(products_obj, data=request.data, partial=True)
        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
        return Response({'Products': serializers.data, 'message': 'Your data is saved successfully'})

    except Exception as e:
        return Response({'message':'Invalid Id'})


@api_view(['DELETE'])
def delete_product(request,id):
    try:
        products_obj = products.objects.get(id=id)
        serializers = productsSerializer(products_obj)
        products_obj.delete()
        return Response({'Products': serializers.data,'message':'Deleted Successfully'})
    except Exception as e:
        return Response({'message':'Invalid Id'})

