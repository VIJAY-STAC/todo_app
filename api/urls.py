
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,TaskLabelsViewset

router = DefaultRouter()
router.register(r"tasks",TaskViewSet,basename="tasks")
router.register(r"tasklabels",TaskLabelsViewset,basename="TaskLabel")
urlpatterns = [
    path('',include(router.urls))
]