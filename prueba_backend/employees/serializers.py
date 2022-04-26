from rest_framework import serializers
from .models import Employee, Gender, WorkedHours

class EmployeeItemSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = ['id', 'gender_id', 'job_id','name', 'last_name', 'birthdate']



class GenderItemSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Gender
        fields = ('__all__')



class WorkedHoursItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkedHours
        fields = ['id', 'employee_id', 'worked_hours', 'worked_date']



class WorkedHoursItemSerializerList(serializers.ModelSerializer):
    class Meta:
        model = WorkedHours
        fields = ['employee_id', 'worked_hours','worked_date']

