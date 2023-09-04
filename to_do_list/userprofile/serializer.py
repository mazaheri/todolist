from rest_framework import serializers

from userprofile.models import Task
from userprofile.models import Category


class TasksSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.title', read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name='single-task')

    class Meta:
        model = Task
        fields = ('user', 'username','title', 'description', 'deadline', 'is_done', 'category_name', 'created_at'
                  , 'updated_at', 'url')


class TaskViewSerializer(serializers.ModelSerializer):
    # category = serializers.ChoiceField(choices=[])
    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'deadline', 'is_done', 'category')

    # def __init__(self, *args, **kwargs):
    #     valid_categories = kwargs.pop('valid_categories', [])
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].choices = [(cat, cat) for cat in valid_categories]