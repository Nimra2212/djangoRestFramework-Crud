from rest_framework import serializers
from todoApp.models import Task


class TaskSerializerv1(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get("request", None)
        if request:
            validated_data["user_id"] = request.user.id

        return super().create(validated_data)

    class Meta:
        model = Task
        fields = ('title', 'complete', 'created')

