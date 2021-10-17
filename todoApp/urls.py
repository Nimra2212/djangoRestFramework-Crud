from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # class base short view url
    path('taskApi', views.TaskListView.as_view()),
    path('taskApi/<int:pk>/', views.TaskDetailView.as_view()),

    # class base function view url
    path('tasksList', views.TaskLists.as_view(), name='task-list'),
    path('taskSingleApi/<int:pk>/', views.TaskDetails.as_view()),

    # function base view url
    path('tasks', views.task_lists, name='tasks'),
    path('task/<str:pk>/', views.task_detail, name='task'),
    path('task-create/', views.task_create, name='task-create'),
    path('task-update/<str:pk>/', views.task_update, name='task-update'),
    path('task-delete/<str:pk>/', views.task_delete, name='task-delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)
