# prueba_backend

## Endpoinst:
## Contrato 1.1
  url:
  http://127.0.0.1:8000/employees/employee-items/ <br />
 request:
  {
    "gender_id": 1, 
    "job_id": 1, 
    "name": "Juan", 
    "last_name": "Pérez", 
    "birthdate": "1983-01-01" 
 }
 
 ## Contrato 1.2
 
 url:
  http://127.0.0.1:8000/employees/worked-hours/ <br />
  request:
  {
    "employee_id": 2, 
    "worked_hours": 10, 
    "worked_date": "2019-01-01" 
}


 ## Contrato 1.3
 
 url:
  http://127.0.0.1:8000/employees/employee-jobs/ <br />
  request:
  
{
    "job_id": 1
}

 ## Contrato 1.4
 
 url:
  http://127.0.0.1:8000/employees/total-worked-hours/ <br />
  request:
  
{
    "employee_id": 1, 
    "start_date": "2019-01-01", 
    "end_date": "2019-06-30"
}


## Contrato 1.5
 
 url:
  http://127.0.0.1:8000/employees/salary-payment/ <br />
  request:
  
{
    "employee_id": 2, 
    "start_date": "2019-01-01", 
    "end_date": "2019-06-30"
}

