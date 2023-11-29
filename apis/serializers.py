from rest_framework import serializers

from .models import Jobs, Employees


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobs
        fields = [
            'job_id',
            'job_title',
            'min_salary',
            'max_salary',
        ]


class EmployeesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = [
            'employee_id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'hire_date',
            'job_id',
            'salary',
            'manager_id',
            'department_id'
        ]
