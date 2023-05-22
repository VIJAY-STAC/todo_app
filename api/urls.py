
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks",TaskViewSet,basename="tasks")
urlpatterns = [
    path('todo/',include(router.urls))
]