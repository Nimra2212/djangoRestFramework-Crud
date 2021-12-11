from rest_framework.permissions import IsAuthenticated

from todoApp.models import Task
from .serializers import TaskSerializerv1
from rest_framework import viewsets


# with Django rest_framework viewsets

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Task.objects.all()
    serializer_class = TaskSerializerv1

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(user_id=self.request.user.id)

