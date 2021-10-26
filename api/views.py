from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import AppUser
from api.serializers import AppUserSerializer

class AppUserApi(APIView):
    def post(self,request):
        print(request.data)
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("User has been created successfully")
            return Response("User has been created successfully",status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        users = AppUser.objects.all()
        serializer = AppUserSerializer(users, many=True)
        return Response(serializer.data)



















# from functools import partial
# from rest_framework import serializers
# from rest_framework.serializers import Serializer
# from api.serializers import AppUserSerializer
# from django.shortcuts import render
# from api.models import AppUser
# from django.http import HttpResponse,Http404,JsonResponse
# from rest_framework.renderers import JSONRenderer
# import io
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt


# from django.utils.decorators import method_decorator
# from django.views import View 
# import json

# @method_decorator(csrf_exempt, name='dispatch')
# class AppUserApi(View):
#     def post(self,request):
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         print(stream)
#         python_data = JSONParser().parse(stream)
#         emailToCheck = python_data.get('email')

#         users = AppUser.objects.all()
#         python = AppUserSerializer(users, many=True)
#         for user in python.data:
#             print(user.get('email'))

        
        
        


#         serialize = AppUserSerializer(data = python_data)
#         if serialize.is_valid():
#             serialize.save()
#             print("Sent")
#             #return JsonResponse({"msg":"created"})
#             res = {'msg' : " created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         print('error')
#         return JsonResponse("error", safe=False)
        

