from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone, dateformat
from .forms import TasksForm
from .models import Tasks
from accounts.models import CustomUser

import datetime

formatdate = lambda date : dateformat.format(date, 'Y-m-d')

@login_required(login_url='accounts:login')
def index(request):
    formatted_date = dateformat.format(timezone.now(), 'Y-m-d')
    url = f'/tasks/{formatted_date}'
    return redirect(url)

@login_required(login_url='accounts:login')
def home(request, date):
    user_id = request.user.id
    tasks = Tasks.objects.filter(user=user_id).filter(date=formatdate(date))
    today = timezone.now().astimezone(timezone.utc).replace(tzinfo=None)
    past = today > date-datetime.timedelta(days=-1)

    return render(request, 'taskboard/home.html', {
        'day': dateformat.format(date, 'd F Y'),
        'daybefore': formatdate(date+datetime.timedelta(days=-1)),
        'dayafter': formatdate(date+datetime.timedelta(days=1)),
        'date': formatdate(date),
        'past': past,
        'tasks': tasks,
        'allowupdate': formatdate(today) == formatdate(date)
    })

@login_required(login_url='accounts:login')
def new(request, date):
    user_id = request.user.id
    date = formatdate(date)
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid(user_id, date):
            task = form.save()
            return redirect('taskboard:home', date)

    form = TasksForm(initial={
        'user': user_id,
        'date': date
    })

    return render(request, 'taskboard/new.html', {'form': form, 'date': date})

@login_required(login_url='accounts:login')
def update(request, date):
    user_id = request.user.id
    if request.method == 'POST':
        task = get_object_or_404(Tasks, pk=int(request.POST['task_id']))
        if task.user.id == user_id and formatdate(task.date) == formatdate(timezone.now()):
            task.completed = not task.completed
            task.save()
    return redirect('taskboard:home', formatdate(date))