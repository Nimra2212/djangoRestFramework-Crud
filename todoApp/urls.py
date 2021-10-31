from django.urls import path
from todoApp.api.v1 import views
from rest_framework.routers import DefaultRouter

from django.urls import include

# from todoApp.api.v1.viewsets import TodoViewSet


from .api.v1.routers import api_urlpatterns1 as api_v1
from .api.v2.routers import urlpatterns1 as api_v2
from .api.v3.routers import urlpatterns2 as api_v3

urlpatterns = [
    path('api/v1/', include(api_v1)),
    path('api/v2/', include(api_v2)),
    path('api/v3/', include(api_v3)),
]




# router = DefaultRouter()
# router.register('api', TodoViewSet, basename='todo')
#
#
# urlpatterns = [
#     # for viewsets url
#     path('', include(router.urls)),
#
#     # class base short view url
#     path('taskApi', viewsets.TaskListView.as_view()),
#     path('taskApi/<int:pk>/', viewsets.TaskDetailView.as_view()),
#
#     # class base function view url
#     path('tasksListTask', viewsets.TaskLists.as_view(), name='task-list'),
#     path('taskSingleApi/<int:pk>/', viewsets.TaskDetails.as_view()),
#
#     # function base view url
#     path('tasks', viewsets.task_lists, name='tasks'),
#     path('task/<str:pk>/', viewsets.task_detail, name='task'),
#     path('task-create/', viewsets.task_create, name='task-create'),
#     path('task-update/<str:pk>/', viewsets.task_update, name='task-update'),
#     path('task-delete/<str:pk>/', viewsets.task_delete, name='task-delete')
# ]

