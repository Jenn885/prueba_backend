from asyncio.windows_events import NULL
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeItemSerializer, GenderItemSerializer, WorkedHoursItemSerializer, WorkedHoursItemSerializerList,GenderItemSerializerSimple
from .models import Employee, Gender, WorkedHours
from Jobs.models import Job
from Jobs.serializers import JobItemSerializer
from django.db.models import Q
from datetime import datetime
import time
from datetime import timedelta, date
from dateutil import relativedelta

# Create your views here.
class EmployeeItemViews(APIView):
    def post(self, request):
        #a,b = 'áéíóúü','aeiouu'
        serializer = EmployeeItemSerializer(data=request.data)
        gender = request.data['gender_id']
        job = request.data['job_id']
        name = request.data['name']
        last_name=request.data['last_name']
        birthdate=request.data['birthdate']

        current_time = datetime.now()
        year, month, day = map(int, birthdate.split('-'))
        date1 = datetime(year, month, day)
        date2 = datetime(current_time.year, current_time.month, current_time.day)
        diff = relativedelta.relativedelta(date2, date1)

        age = diff.years
        

        if not Gender.objects.filter(id=gender).exists() or not  Job.objects.filter(id=job).exists() or (Employee.objects.filter(name=name).exists() and Employee.objects.filter(last_name=last_name).exists()) or age<18:
            
            """
            error1=''
            error2=''
            error3=''
            error4=''
            
            if Employee.objects.filter(name=name).exists() and Employee.objects.filter(last_name=last_name).exists():
                error1='Employee name already exists. '
            
            if not Gender.objects.filter(id=gender).exists():
                error2='Gender does not exist. '

            if not Job.objects.filter(id=job).exists():
                error3  ='Job does not exist. '
            
            if age<18:
                error4 ='The employee must be of legal age '
            errors={
                "message": error1+error2+error3+error4
            }
            return Response(errors)"""
            return Response({ "id": None, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response({ "id": serializer.data['id'], "sucess": True}, status=status.HTTP_200_OK)
                
            else:
                return Response({ "id": None, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)


class WorkedHoursItemViews(APIView):
    def post(self, request):
        serializer = WorkedHoursItemSerializer(data=request.data)
        employee = request.data['employee_id']
        worked_hours=request.data['worked_hours']
        worked_date=request.data['worked_date']

        first_date = worked_date
        second_date = datetime.now()

        formatted_date1 = time.strptime(first_date, '%Y-%m-%d')
        formatted_date2 = time.strptime(str(second_date.year)+'-'+str(second_date.month)+'-'+str(second_date.day), '%Y-%m-%d')  
   
        if (formatted_date1 <= formatted_date2) and worked_hours<20 and Employee.objects.filter(id=employee).exists() and not WorkedHours.objects.filter(employee_id=employee, worked_date=worked_date).exists():
            
            if serializer.is_valid():
                serializer.save()
                return Response({ "id": serializer.data['id'], "sucess": True}, status=status.HTTP_200_OK)
            else:
                return Response({ "id": None, "sucess":False}, status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({ "id": None, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)
           


class EmployeeJobItemViews(APIView):
    def post(self, request):

        job = request.data['job_id']

        items = Employee.objects.all().filter(job_id=job)
        serializer = EmployeeItemSerializer(items, many=True)
        data=serializer.data
        
        list_complete=[]
        for d in data:
            item_job = Job.objects.get(id=d['job_id'])
            serializer_job = JobItemSerializer(item_job)
            item_gender = Gender.objects.get(id=d['gender_id'])
            serializer_gender = GenderItemSerializer(item_gender)

            original_date = datetime.strptime(d['birthdate'], '%Y-%m-%d')
            formatted_date = original_date.strftime("%d-%m-%Y")
            dicc={

                "id": d['id'],
                "name": d['name'],
                "last_name": d['last_name'],
                "birthdate":formatted_date,
                "job": { 
                    "id":serializer_job.data['id'],
                    "name":serializer_job.data['name'],
                    "salary":serializer_job.data['salary']
                    
                },
                "gener": { 
                    "id":serializer_gender.data['id'],
                    "name":serializer_gender.data['name'],

                    
                },
            }
            list_complete.append(dicc)

        

        if not Employee.objects.filter(job_id=job).exists():
          
            return Response({ "employees":[ None], "sucess": False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            
            return Response({ "employees": list_complete, "sucess": True}, status=status.HTTP_400_BAD_REQUEST)

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
                
class TotalWorkedHoursItemViews(APIView):
    def post(self, request):
        employee = request.data['employee_id']
        start_date=request.data['start_date']
        end_date=request.data['end_date']
        
        year1, month1, day1 = map(int, start_date.split('-'))
        date1 = datetime(year1, month1, day1)
        year2, month2, day2 = map(int, end_date.split('-'))
        date2 = datetime(year2, month2, day2)

        original_date1 = datetime.strptime(start_date, '%Y-%m-%d')
        formatted_date1 = original_date1.strftime("%d-%m-%Y")
        original_date2 = datetime.strptime(end_date, '%Y-%m-%d')
        formatted_date2 = original_date2.strftime("%d-%m-%Y")
        
        
      

        if Employee.objects.filter(id=employee).exists() and formatted_date1<formatted_date2 :
            items = WorkedHours.objects.all().filter(employee_id=employee)
            serializer = WorkedHoursItemSerializer(items, many=True)
            data=serializer.data
            worked_hours=0
            for dt in daterange(date1, date2):
                for d in data:
               # d['worked_date']=datetime.strptime(str(d['worked_date']), '%Y-%m-%d')
                    if d['worked_date']==dt.strftime("%Y-%m-%d"):
                        worked_hours+=int(d['worked_hours'])
            return Response({ "total_worked_hours": worked_hours, "sucess": True}, status=status.HTTP_200_OK)
              
        else:
            return Response({ "total_worked_hours": None, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)
        
    
class SalaryPaymentItemViews(APIView):
    def post(self, request):
        employee = request.data['employee_id']
        start_date=request.data['start_date']
        end_date=request.data['end_date']
        
        year1, month1, day1 = map(int, start_date.split('-'))
        date1 = datetime(year1, month1, day1)
        year2, month2, day2 = map(int, end_date.split('-'))
        date2 = datetime(year2, month2, day2)

        diff = relativedelta.relativedelta(date2, date1)
        total_months = diff.months
        

        original_date1 = datetime.strptime(start_date, '%Y-%m-%d')
        formatted_date1 = original_date1.strftime("%d-%m-%Y")
        original_date2 = datetime.strptime(end_date, '%Y-%m-%d')
        formatted_date2 = original_date2.strftime("%d-%m-%Y")


        if Employee.objects.filter(id=employee).exists() and formatted_date1<formatted_date2 :
            item_employee = Employee.objects.get(id=employee)
            serializer_employee = EmployeeItemSerializer(item_employee)
            items = Job.objects.get(id=serializer_employee.data['job_id'])
            serializer = JobItemSerializer(items)
            data=serializer.data

            payment=total_months*float(data['salary'])
            return Response({ "payment": payment, "sucess": True}, status=status.HTTP_200_OK)
              
        else:
            return Response({ "payment": None, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)
        



class GenderListItemViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Gender.objects.get(id=id)
            serializer = GenderItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Gender.objects.all()
        serializer = GenderItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

           
class GenderItemsViews(APIView):
     def post(self, request):
        
        serializer = GenderItemSerializerSimple(data=request.data)
        name = request.data['name']
        
        if Gender.objects.filter(name=name).exists():
         
            return Response({ "id": None, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response({ "id": serializer.data['id'], "sucess": True}, status=status.HTTP_200_OK)
                
            else:
                return Response({ "id": serializer.errors, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)

    

class EmployeesListItemViews(APIView):
    
    def get(self, request, id=None):
        if id:
            item = Employee.objects.get(id=id)
            serializer = EmployeeItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Employee.objects.all()
        serializer = EmployeeItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    