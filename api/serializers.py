from rest_framework import serializers
from .models import Task, TaskLabels

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = (
            "id",
            "name",
            "date_time",
            "status",
            "description",
            "task_label"
        )

class TaskLabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLabels
        fields = "__all__"