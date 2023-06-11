import datetime
from django.shortcuts import render


from .models import Task, TaskLabels
from .serializers import TaskLabelsSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class TaskViewSet(viewsets.ModelViewSet):
    model = Task
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self, request):
        id = request.user.id
        queryset = Task.objects.filter(created_by_id=id).order_by('-created_at')
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save(created_by=request.user)
        serializer = TaskSerializer(task)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        id = request.user.id
        queryset = Task.objects.filter(created_by_id=id).order_by('-created_at')
        serializer = TaskSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        task_id = kwargs['pk']  # Get the task ID from the URL parameter
        
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": f"Task with ID {task_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has permission to update the task
        if task.created_by != request.user:
            return Response({"error": "You don't have permission to update this task."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = TaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_task = serializer.save()

        serializer = TaskSerializer(updated_task)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        task_id = kwargs['pk']  # Get the task ID from the URL parameter
        
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": f"Task with ID {task_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has permission to update the task
        if task.created_by != request.user:
            return Response({"error": "You don't have permission to delete this task."}, status=status.HTTP_403_FORBIDDEN)
        task.delete()
        return Response({"Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['get'])
    def tasklabels(self, request, *args, **kwargs):
        tasklabels = Task.objects.all().values_list('task_label').distinct()
        return Response(tasklabels, status=status.HTTP_200_OK)


class TaskLabelsViewset(viewsets.ModelViewSet):
    model = TaskLabels
    serializer_class = TaskLabelsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        queryset = TaskLabels.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = TaskLabelsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
       

    def list(self, request, *args, **kwargs):
        tasklabels = TaskLabels.objects.all()
        serializer = TaskLabelsSerializer(tasklabels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        id = kwargs['pk']
        try:
            tasktype =  TaskLabels.objects.get(id=id)
            print()
        except:
            return Response({"error":"Task type of does not accept."},status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskLabelsSerializer(tasktype, data=request.data)
        serializer.is_valid(serializer)
        tasklable = serializer.save(last_modified_by=request.user)
        serializer = TaskLabelsSerializer(tasklable)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        return Response({},status=status.HTTP_405_METHOD_NOT_ALLOWED)