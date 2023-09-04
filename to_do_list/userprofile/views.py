from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from userprofile.models import Task


@login_required(login_url='/userprofile/login/')
def profile(request):
    todolist = Task.objects.filter(user=request.user)
    context =' <br>'.join([f"name: {task.title} / deadline: {task.deadline} / status: {task.is_done}" for task in todolist])
    return HttpResponse(context)


def login(request):
    return HttpResponse('You need Login To see this page')


def signup(request):
    return HttpResponse('signup page')

