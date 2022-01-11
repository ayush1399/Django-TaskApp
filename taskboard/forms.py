from django.forms import ModelForm
from .models import Tasks
from django.forms.widgets import EmailInput

# Create the form class.
class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['description', 'user', 'date']#, 'date']

    def is_valid(self, user_id, date):
        valid = super(TasksForm, self).is_valid()
        
        if self.data['user'] == str(user_id) and self.data['date'] == date:
            return True
        else:
            return False