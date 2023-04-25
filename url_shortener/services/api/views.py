from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from ..models import Url
from .serializers import URLSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.authtoken.models import Token
import random,string
# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def url_api(request):
    if request.method == 'GET':
        
        urls = Url.objects.filter(user=request.user)
        if urls.exists():
            serializer = URLSerializer(urls, many=True)
            for ser in serializer.data:
                ser['shortened_path'] = f"{get_current_site(request)}{ser['alias']}"
            # serializer.data[0]['path'] = 'subham'
            return Response(serializer.data)
        else:
            return Response({'detail': 'No URL found for this user.'}, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'POST':

        token_value = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        token = Token.objects.get(key=token_value)
        serializer_data = request.data.copy()
        serializer_data['user'] = token.user.pk
        
        if serializer_data['alias'] == "":
            alias = getAlias()
            serializer_data['alias'] = alias
        
        
        serializer = URLSerializer(data =  serializer_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'details': serializer_data ,'shortened_path': f"{get_current_site(request)}{serializer_data['alias']}"})
        else:
            return Response(serializer.errors)
    
    # if request.method == 'PUT':
    #     id = request.data.get('id')
    #     stu = Student.objects.get(id=id)
    #     serializer = StudentSerializer(stu, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Data Updated'})
    #     else:
    #         return Response(serializer.errors)
    
    # if request.method == 'DELETE':
    #     id = request.data.get('id')
    #     stu = Student.objects.get(id=id)
    #     stu.delete()
    #     return Response({'msg': 'Data Deleted'})


def getAlias():
    return "".join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8) ])
