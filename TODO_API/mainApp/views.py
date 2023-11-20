from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

#Get all data from the database
@api_view(['GET'])
def all_todoList(request):
    todo_obj = mytodo.objects.all()
    serializers = mytodoserialiser(todo_obj,many=True)
    return Response({'TO DO List': serializers.data})


#Get single data from the database
@api_view(['GET'])
def single_todoList(request,id):
    try:
        todo_obj = mytodo.objects.get(id=id)
        serializers = mytodoserialiser(todo_obj)
        return Response({'TO DO List': serializers.data})
    except Exception as e:
        return Response({'Error':'Invalid Id'})


# Insert single data into database
@api_view(['POST'])
def insert_todo(request):
    serializers = mytodoserialiser(data=request.data)

    if not serializers.is_valid():
        return Response({'Error': serializers.errors, 'message':'Something went wrong.'})
    else:
        serializers.save()
    return Response({'TO DO List': serializers.data, 'message':'Data inserted Successfully'})


#Update data into database
@api_view(['PATCH','PUT'])
def edit_todo(request,id):
    try:
        todo_obj = mytodo.objects.get(id=id)

        serializers = mytodoserialiser(todo_obj, data=request.data, partial=True)

        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Something went wrong.'})
        else:
            serializers.save()
        return Response({'TO DO List': serializers.data, 'message':'Data Updated Successfully'})
    
    except Exception as e:
        return Response({'Error':'Invalid Id'})


#Delete single data from the database
@api_view(['DELETE'])
def delete_todo(request,id):
    try:
        todo_obj = mytodo.objects.get(id=id)
        serializers = mytodoserialiser(todo_obj)
        todo_obj.delete()
        return Response({'TO DO List': serializers.data, 'message':'Data deleted Successfully'})
    except Exception as e:
        return Response({'Error':'Invalid Id'})
    

