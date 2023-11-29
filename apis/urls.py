from django.urls import path, include
from rest_framework import routers
from .views import JobsViewSet, ManagerEmployeesViewSet

router = routers.DefaultRouter()
router.register(r'jobs', JobsViewSet)
router.register(r'employees', ManagerEmployeesViewSet)


urlpatterns = [
    path('', include(router.urls))
]
