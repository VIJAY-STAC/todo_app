import uuid
from django.db import models
from django.conf import settings

from .core import CreatedByModel, LastModifiedByModel, PrimaryUUIDTimeStampedModel

TASK_STATUS=(
    ('completed','completed'),
    ('pending','pending'),
    ('start','start')
)



# Create your models here.

class TaskLabels(PrimaryUUIDTimeStampedModel, CreatedByModel, LastModifiedByModel):
    task_label = models.CharField(max_length=30, null=True,blank=True)

    def __str__(self):
        return self.task_label
class Task(PrimaryUUIDTimeStampedModel, CreatedByModel, LastModifiedByModel):
    # task_label=models.ForeignKey(TaskLabels,
    #                              on_delete=models.SET_NULL,
    #                              null=True,
    #                              blank=True)

    task_label = models.CharField(max_length=30, null=True,blank=True, default='other')
    name = models.CharField(null=False,max_length=20)
    date_time = models.DateTimeField(null=True,blank=False)
    status = models.CharField(max_length=10,choices=TASK_STATUS,default='pending')
    description = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name



    
    