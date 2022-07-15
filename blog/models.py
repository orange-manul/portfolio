from datetime import datetime
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    descrpition = models.TextField(max_length=150)
    date_of_time = models.DateField(auto_now=False)

    def __str__(self):
        return self.title