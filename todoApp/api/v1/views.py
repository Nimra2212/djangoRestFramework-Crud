from rest_framework import status, generics
from todoApp.models import Task
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import TaskSerializerv1
from rest_framework import viewsets


# with Django rest_framework viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerv1

