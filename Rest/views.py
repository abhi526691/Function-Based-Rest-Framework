from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MyDataSerializer, RegisterSerializer
from .models import MyData
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.


@api_view(['POST', 'GET'])
def register_user(request):
    serializer = RegisterSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'User Account Created Successfully'
        data['email'] = user.email
        data['username'] = user.username
        token = Token.objects.get(user=user).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)





@api_view(['GET'])
def index(request):
    myDict = {
        "Name" : "Abhishek Pandey",
        "Class" : "Bachelor",
        "Post" : "System Engineer Specialist"
    }
    return Response(myDict)


@api_view(['GET'])
def getAllData(request):
    mydataObj = MyData.objects.all()
    serializer = MyDataSerializer(mydataObj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDetail(request, id):
    mydataObj = MyData.objects.get(id=id)
    serializer = MyDataSerializer(mydataObj)
    return Response(serializer.data)

@api_view(['POST'])
def createDetail(request):
    serializer = MyDataSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteDetail(request, id):
    serializer = MyData.objects.get(id = id)
    serializer.delete()
    return JsonResponse("Deleted Successfully", safe=False)

@api_view(['POST'])
def updateData(request, id):
    mydatObj = MyData.objects.get(id=id)
    serializer = MyDataSerializer(instance=mydatObj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)