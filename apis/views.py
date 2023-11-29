from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import JobsSerializer, EmployeesSerializers
from .models import Jobs, Employees


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


class ManagerEmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers

    def list(self, request, *args, **kwargs):
        employee = request.query_params.get('manager_id', None)
        print("#########")
        if employee:
            print("#########")
            self.queryset = self.queryset.filter(manager_id__isnull=True)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_employees = Employees.objects.filter(manager_id=instance.employee_id).exclude(manager_id=instance.manager_id)
        related_serializer = EmployeesSerializers(related_employees, many=True)
        return Response({
            'employee': serializer.data,
            'related_eployees': related_serializer.data
        })
