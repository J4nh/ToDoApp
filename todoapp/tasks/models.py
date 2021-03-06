from django.db import models
from datetime import datetime
from datetime import date

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def is_end_date(self):
        return date.today() > self.end_date.date()

    def __str__(self):
        return self.title
        