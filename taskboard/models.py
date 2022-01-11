from django.conf import settings
from django.db import models

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.description