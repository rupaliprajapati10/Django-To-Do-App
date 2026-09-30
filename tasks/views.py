from django.shortcuts import render, redirect
from .models import Task


def home(request):
    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Task.objects.create(title=title)

        return redirect("home")

    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"tasks": tasks})


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()

    return redirect("home")


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect("home")