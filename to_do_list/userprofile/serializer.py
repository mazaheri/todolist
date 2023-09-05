from rest_framework import serializers

from userprofile.models import Task
from userprofile.models import Category


class TasksSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.title', read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name='single-task')
    task_id = serializers.ReadOnlyField(source='pk')


    class Meta:
        model = Task
        fields = ('task_id','user', 'username','title', 'description', 'deadline', 'is_done', 'category_name', 'created_at'
                  , 'updated_at', 'url')


class TaskViewSerializer(serializers.ModelSerializer):
    task_id = serializers.ReadOnlyField(source='pk')
    category_name = serializers.CharField(source='category.title', read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Task
        fields = (
        'task_id', 'user', 'username', 'title', 'description', 'deadline', 'is_done', 'category_name', 'created_at'
        , 'updated_at')
