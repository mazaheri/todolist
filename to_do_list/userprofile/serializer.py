from rest_framework import serializers

from userprofile.models import Task


class TaskSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.title', read_only=True)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ('username','title', 'description', 'deadline', 'is_done', 'category_name')