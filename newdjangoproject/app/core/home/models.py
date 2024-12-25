from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    stream=models.CharField(max_length=100)
    email=models.EmailField(default="1")