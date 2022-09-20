from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .Serializers import ApplicationSerializer
from .models import *
# Create your views here.

class ApplicationList(APIView):

    def get(self,request):
        User1 = User.objects.all()
        serializer = ApplicationSerializer(User1, many= True)
        return Response(serializer.data)
    
    def post(self):
        pass

    
class ApplicationList2(APIView):
    def get(self,request):
        Customer1 = Customer.objects.all()
        serializer = ApplicationSerializer(Customer1, many= True)
        return Response(serializer.data)

    def post(self):
        pass
    