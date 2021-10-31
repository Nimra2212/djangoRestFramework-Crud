from rest_framework import serializers
from todoApp.models import Task


class TaskSerializerv3(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
