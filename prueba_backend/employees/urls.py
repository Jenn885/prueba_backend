from django.urls import path

from .views import EmployeeItemViews, GenderListItemViews, EmployeeJobItemViews, WorkedHoursItemViews, TotalWorkedHoursItemViews, SalaryPaymentItemViews,EmployeesListItemViews,GenderItemsViews

urlpatterns=[
    path('employee-items/', EmployeeItemViews.as_view()),
    path('list-gender/<int:id>', GenderListItemViews.as_view()),
    path('gender-items/', GenderItemsViews.as_view()),
    path('employee-jobs/', EmployeeJobItemViews.as_view()),
    path('worked-hours', WorkedHoursItemViews.as_view()),
    path('total-worked-hours', TotalWorkedHoursItemViews.as_view()),
    path('salary-payment/',SalaryPaymentItemViews.as_view()),
    path('employees-list/<int:id>', EmployeesListItemViews.as_view())
]