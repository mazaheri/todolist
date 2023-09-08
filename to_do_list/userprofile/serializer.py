from django.contrib.auth.models import User
from rest_framework import serializers

from userprofile.models import Task


class TasksSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name='single-task')
    task_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Task
        fields = ('task_id', 'user', 'username', 'title', 'description', 'deadline', 'is_done', 'category_name',
                  'created_at', 'updated_at', 'url')


class TaskViewSerializer(serializers.ModelSerializer):
    task_id = serializers.ReadOnlyField(source='pk')
    category_name = serializers.CharField(source='category.title', read_only=True)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = (
            'task_id', 'user', 'username', 'title', 'description', 'deadline',
            'is_done', 'category_name', 'created_at', 'updated_at',
        )


class UpdateTaskSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    deadline = serializers.DateTimeField(required=False)
    is_done = serializers.BooleanField(required=False)
    category = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        for key in validated_data:
            setattr(instance, key, validated_data.get(key))
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']
