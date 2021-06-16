from django.db import models

class ToDo(models.Model):
    date_added = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=200)
