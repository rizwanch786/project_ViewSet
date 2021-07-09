from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers, status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Created Successfully'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_201_CREATED)

    def retrieve(self, request, pk = None):
        if pk is not None:
            stu = Student.objects.get(id = pk)
            serializer = StudentSerializer(stu)
            return(serializer)
    
    def update(self, request, pk = None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Updated'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, pk = None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Updated'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk = None):
            stu = Student.objects.get(id = pk)
            stu.delete()
            return Response({'msg': 'Data Delete Successfully'})