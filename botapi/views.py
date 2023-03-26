from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class ProductsView(APIView):
    def get(self, request):
        products = ProductsModel.objects.all()
        serializer = ProductsSerializer(products, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductByIdView(APIView):
    def get(self, request, pk):
        products = ProductsModel.objects.filter(pk=pk)
        serializer = ProductsSerializer(products, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InfoView(APIView):
    def get(self, request):
        info = InfoModel.objects.all()
        serializer = InfoSerializer(info, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersView(APIView):
    def post(self, request):
        serializer = CustomUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)