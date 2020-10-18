from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.

def index(request):

    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            items = List.objects.all()
            items = List.objects.order_by('-created')
            messages.success(request, "Todo item added successfully")
            return redirect('/')
    else:
        items = List.objects.all() 
        items = List.objects.order_by('-created')
        return render(request, 'todo_app/index.html', {'items':items})

def update_todo(request, pk):
    todo = List.objects.get(id=pk)
    form = ListForm
    if request.method == "POST":
        form = ListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo item updated successfully")
    return redirect('/')


def mark_completed(request, pk):
    todo = List.objects.get(id=pk)
    todo.completed = True
    todo.save()
    messages.success(request, 'Todo item marked completed')

    return redirect('/')

def unmark(request, pk):
    todo = List.objects.get(id=pk)
    todo.completed = False
    todo.save()
    messages.success(request, 'Todo item marked uncompleted')

    return redirect('/')

def delete_todo(request, pk):
    todo = List.objects.get(id=pk)
    todo.delete()
    messages.error(request, 'Todo item deleted')

    return redirect('/')

