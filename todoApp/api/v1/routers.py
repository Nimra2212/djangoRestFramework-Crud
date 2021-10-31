from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

router1 = routers.DefaultRouter()
router1.register('apitodoviewset', views.TodoViewSet, basename='todoapp')

api_urlpatterns1 = router1.urls
