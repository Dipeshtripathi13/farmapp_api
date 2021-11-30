from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ptarkalis
from .serializers import ptarkalisSerializer

# Create your views here.

class ptarkaliList(APIView):
    def get(self, request):
        ptarkalis1 = ptarkalis.objects.all()
        serializer= ptarkalisSerializer(ptarkalis1, many=True)
        return Response(serializer.data)

    def post(self):
        pass