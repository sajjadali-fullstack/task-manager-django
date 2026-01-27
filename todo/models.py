from django.db import models


# Create your models here.

class Task(models.Model):
    # task, is_complete, created_at, updated_at
    task = models.CharField(max_length=786)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.task
