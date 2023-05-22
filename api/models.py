import uuid
from django.db import models

TASK_STATUS=(
    ('completed','completed'),
    ('pending','pending'),
    ('start','start')
)

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True



class PrimaryUUIDModel(models.Model):
    # id = models.AutoField(primary_key=True,)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    
    class Meta(object):
        abstract = True

class PrimaryUUIDTimeStampedModel(PrimaryUUIDModel, TimeStampedModel):
    class Meta(object):
        abstract = True


class Task(PrimaryUUIDTimeStampedModel):
    name = models.CharField(null=False,max_length=20)
    date_time = models.DateTimeField(null=True,blank=False)
    status = models.CharField(max_length=10,choices=TASK_STATUS,default='pending')
    description = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name