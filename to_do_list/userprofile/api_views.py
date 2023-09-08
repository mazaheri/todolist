"""
    docstring
"""
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from userprofile.models import Task
from userprofile.serializer import TasksSerializer, TaskViewSerializer, UpdateTaskSerializer, UserSerializer


class RegistrationView(APIView):
    def post(self, request):
        """
        :param request:
        :return:
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide both username and password.'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password, is_active=True)

        "Now show tokens for new user in response"
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.validated_data
            response_data['user_id'] = user.id
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TasksSerializer
    queryset = Task.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ('title', 'description')
    ordering_fields = ('title', 'deadline', 'created_at')
    filterset_fields = ('category', 'is_done')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskViewAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskViewSerializer

    def get(self, request, pk):
        obj = get_object_or_404(Task, pk=pk, user=request.user)
        data = self.serializer_class(instance=obj).data
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        obj = get_object_or_404(Task, pk=pk, user=request.user)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = UpdateTaskSerializer(task, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(self.serializer_class(instance=task).data, status=status.HTTP_200_OK)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()  # Retrieve all users
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
