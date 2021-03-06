from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

app_name = 'main'

@login_required(login_url='accounts:login')
def index(request):
    return redirect('taskboard:index')