from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from userprofile.models import Task
from userprofile.serializer import TaskSerializer


@login_required(login_url='/userprofile/login/')
def profile(request):
    todolist = Task.objects.filter(user=request.user)
    context =' <br>'.join([f"name: {task.title} / deadline: {task.deadline} / status: {task.is_done}" for task in todolist])
    return HttpResponse(context)


def login(request):
    return HttpResponse('You need Login To see this page')


def signup(request):
    return HttpResponse('signup page')


class TaskListAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('title', 'description')
    ordering_fields = ['title']


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
