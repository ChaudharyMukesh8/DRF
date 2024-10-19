from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# @api_view()  # by default get method calls
# def hello_world(request):
#         return Response("msg: Hello World welcome to the world of django rest framework..")

# @api_view(['GET'])
# def hello_world(request):
#         return Response("msg: Hello World welcome to the world of django rest framework..")

# @api_view(['POST'])
# def hello_world(request):
#         if request.method == 'POST':
#                 print(request.data)
#                 return Response("msg: Hello World welcome to the world of django rest framework post method..")

# OR we can write the get and post method both together.

@api_view(['GET','POST'])
def hello_world(request):
        if request.method == 'GET':
                return Response({"msg: Hello World this is get method"})
        if request.method == 'POST':
                print(request.data)
                return Response({'msg' : 'Hello World welcome to the world of django rest framework post method..','data': request.data})