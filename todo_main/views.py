from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')

    completed_Task = Task.objects.filter(is_completed=True)
    params = {
        'tasks':tasks,
        'completed_task':completed_Task
    }
    return render(request, 'home.html', params)


