import datetime
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all().order_by('-created_at')
        return queryset

    @action(detail=False, methods=['get'])
    def coding(self, request, *args, **kwargs):
        time = datetime.datetime.now()
        return Response({"data":time},status=status.HTTP_200_OK)