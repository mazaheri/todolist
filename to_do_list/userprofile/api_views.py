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
from userprofile.serializer import TasksSerializer, TaskViewSerializer


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
    #
    #
    # def get_queryset(self):
    #     return Task.objects.filter(user=self.request.user)

    def get(self, request, pk):
        obj = get_object_or_404(Task, pk=pk, user=request.user)
        data = self.serializer_class(instance=obj).data
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        obj = get_object_or_404(Task, pk=pk, user=request.user)
        obj.delete()
        return Response(status=status.H)




    # def valid_categories(self):
    #     user = self.request.user
    #     valid_categories = Category.objects.filter(user=user).values('title')
    #     return valid_categories



    # def get_serializer_context(self):
    #     # Include valid_categories in the context
    #     context = super().get_serializer_context()
    #     context['valid_categories'] = self.valid_categories()
    #     return context