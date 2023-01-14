from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='users/sign_in')
def todoForm(request):
    form = TodoForm()
    if request.method == 'POST':
        Todo.objects.create(
            title=request.POST.get('title'),
            user=request.user
        )
    todos = Todo.objects.filter(user=request.user)
    todo = request.GET.get('todo')
    if todo:
        Todo.objects.get(pk=todo).delete()
        return redirect('todo')
    return render(request, 'todo_form.html', {"form": form, 'todos': todos})


def edit_todos(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo')
    return render(request, 'edit_todo.html', {'form': form})
