from typing import List, Union

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
from django.urls import path, URLResolver, URLPattern

urlpatterns2 = [
    path('', views.TaskLists.as_view(), name='task-list'),
    path('taskSingleApi/<int:pk>/', views.TaskDetails.as_view()),
]

