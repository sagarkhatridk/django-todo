from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")

def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = Task.objects.get(pk=pk)

    if request.method == "POST":
        updated_task = request.POST['task']
        get_task.task = updated_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task
        }
        return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')