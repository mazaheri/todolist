from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from userprofile.models import Task, Category
from userprofile.serializer import TasksSerializer, TaskViewSerializer, UpdateTaskSerializer


class TaskListAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TasksSerializer
    queryset = Task.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ('title', 'description')
    ordering_fields = ('title', 'deadline','created_at')
    filterset_fields = ('category', 'is_done')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# class TaskViewAPI(APIView):
class TaskViewAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskViewSerializer
    # queryset = Task.objects.all()

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

