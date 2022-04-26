from django.urls import path

from .views import JobListItemViews, JobItemsViews

urlpatterns=[
   path('', JobListItemViews.as_view()),
   path('job-item/', JobItemsViews.as_view()),
  
]