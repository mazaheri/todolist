from rest_framework import serializers

from userprofile.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline', 'is_done', 'category')