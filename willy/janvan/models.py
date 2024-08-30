from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20, unique=True)
    password=models.CharField(max_length=10, default="")

    def __str__(self):
        return self.username
    