from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VacationSerializer
from vacation.models import Vacation

@api_view(['GET'])
def apiOverView(request):
    api_urls={
        'List':'/vacation-list',
        'Vacation View':'/vacation-detail/<str:pk>/',
        'Create':'/vacation-create',
        'Update':'/vacation-update/<str:pk>/',
        'Delete':'/vacation-delete/<str:pk>/',

        'Vacuser':'/vacation-user-api',
    }
    return Response(api_urls)
@api_view(['GET'])
def vacuser(request):
    owner = request.user.id
    vacations = Vacation.objects.filter(owner=request.user)
    serializer =VacationSerializer(vacations,many=True)
    return Response({"data":serializer.data})

@api_view(['GET'])
def vacationList(request):
    vacations=Vacation.objects.all()
    serializer =VacationSerializer(vacations,many=True)
    return Response({"data":serializer.data})

@api_view(['GET'])
def vacationDetail(request,pk):
    vacations=Vacation.objects.get(pk=pk)
    serializer =VacationSerializer(vacations,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def vacationCreate(request):
    serializer =VacationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def vacationUpdate(request,pk):
    vacation=Vacation.objects.get(pk=pk)

    serializer =VacationSerializer(instance=vacation,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def vacationDelete(request,pk):
    vacation=Vacation.objects.get(pk=id)
    vacation.delete()
    return Response("Item deleted")