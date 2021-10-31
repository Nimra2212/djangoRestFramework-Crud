from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from django.urls import path

urlpatterns1 = [
    # class base short view url
     path('', views.TaskListView.as_view()),
     path('taskApi/<int:pk>/', views.TaskDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns1)