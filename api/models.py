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


class Task(PrimaryUUIDTimeStampedModel, CreatedByModel, LastModifiedByModel):
    name = models.CharField(null=False,max_length=20)
    date_time = models.DateTimeField(null=True,blank=False)
    status = models.CharField(max_length=10,choices=TASK_STATUS,default='pending')
    description = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name