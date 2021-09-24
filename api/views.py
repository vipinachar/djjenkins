from django.shortcuts import render
from functools import partial
from rest_framework import serializers
from rest_framework.serializers import Serializer
from api.serializers import AppUserSerializer
from django.shortcuts import render
from api.models import AppUser
from django.http import HttpResponse,Http404,JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


from django.utils.decorators import method_decorator
from django.views import View 

@method_decorator(csrf_exempt, name='dispatch')
class AppUserApi(View):
    def post(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialize = AppUserSerializer(data = python_data)
        if serialize.is_valid():
            serialize.save()
            print("Sent")
            return JsonResponse("created", safe=False)

