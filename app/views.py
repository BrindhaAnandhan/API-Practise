from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def SchoolViews(request):
    SO = School.objects.all()
    JSO = SchoolModelsSerial(SO, many = True)
    JSD = JSO.data
    return Response(JSD)