from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user_id = models.IntegerField(max_length=100, default=1)
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


# Create your models here.
