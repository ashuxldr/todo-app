from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import *


# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'task/base.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'task/updateTask.html', context)


def delete(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'task/delete.html', context)
