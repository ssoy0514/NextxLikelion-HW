from django.shortcuts import render, redirect
from matplotlib.pyplot import title
from .models import Todo
from datetime import datetime
# Create your views here.
def home(request):
    todos = Todo.objects.all().order_by('deadline')
    for todo in todos:
        diff_date = todo.deadline - datetime.date(datetime.now())
        todo.remain = diff_date.days

    return render(request, 'home.html', {'todos':todos})

def new(request):
    if request.method == "POST":
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail',new_todo.pk)
    return render(request,'new.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk= todo_pk)

    return render(request, 'detail.html',{'todo':todo})

def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    if request.method == "POST":
        Todo.objects.filter(pk=todo_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail',todo_pk)
    return render(request,'edit.html',{'todo':todo})

def delete(request,todo_pk):
    todo=Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect('home')
