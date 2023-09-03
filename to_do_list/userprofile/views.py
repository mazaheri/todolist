from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from userprofile.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
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

class TaskListAPI(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all().values('title')
        serializer = TaskSerializer(tasks, many=True)
        return Response(tasks)

    def post(self, request, *args, **kwargs):
        tasks = Task.objects.all().values('title')
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
