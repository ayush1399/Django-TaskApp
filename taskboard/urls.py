from django.urls import path, register_converter
from datetime import datetime
from . import views

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')
 
app_name = 'taskboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('<yyyy:date>/', views.home, name='home'),
    path('<yyyy:date>/new/', views.new, name='new'),
    path('<yyyy:date>/update', views.update, name='update')
]
