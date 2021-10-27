from django.urls import path
from . import viewsets
from rest_framework.routers import DefaultRouter

from django.urls import include

from .viewsets import TodoViewSet

router = DefaultRouter()
router.register('api', TodoViewSet, basename='todo')


urlpatterns = [
    # for viewsets url
    path('', include(router.urls)),

    # class base short view url
    path('taskApi', viewsets.TaskListView.as_view()),
    path('taskApi/<int:pk>/', viewsets.TaskDetailView.as_view()),

    # class base function view url
    path('tasksListTask', viewsets.TaskLists.as_view(), name='task-list'),
    path('taskSingleApi/<int:pk>/', viewsets.TaskDetails.as_view()),

    # function base view url
    path('tasks', viewsets.task_lists, name='tasks'),
    path('task/<str:pk>/', viewsets.task_detail, name='task'),
    path('task-create/', viewsets.task_create, name='task-create'),
    path('task-update/<str:pk>/', viewsets.task_update, name='task-update'),
    path('task-delete/<str:pk>/', viewsets.task_delete, name='task-delete')
]

