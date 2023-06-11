from django.contrib import admin
from .models import Task,TaskLabels

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','name','task_label','date_time','status','description']

@admin.register(TaskLabels)
class TaskLabelsAdmin(admin.ModelAdmin):
    list_display= ['id','task_label']