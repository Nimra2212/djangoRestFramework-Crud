from todoApp.models import Task
from .serializers import TaskSerializerv1
from rest_framework import viewsets


# with Django rest_framework viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerv1

