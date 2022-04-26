from django.urls import path

from .views import EmployeeItemViews, GenderItemViews, EmployeeJobItemViews, WorkedHoursItemViews, TotalWorkedHoursItemViews, SalaryPaymentItemViews

urlpatterns=[
    path('employee-items/', EmployeeItemViews.as_view()),
    path('gender-items/', GenderItemViews.as_view()),
    path('employee-jobs/', EmployeeJobItemViews.as_view()),
    path('worked-hours', WorkedHoursItemViews.as_view()),
    path('total-worked-hours', TotalWorkedHoursItemViews.as_view()),
    path('salary-payment/',SalaryPaymentItemViews.as_view()),
]