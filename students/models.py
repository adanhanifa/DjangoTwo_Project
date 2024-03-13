from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    body = models.TextField()
    def __str__(self):
        return self.name
