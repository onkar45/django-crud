from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number = models.IntegerField()
    name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=256)
    # marks = models.ManyToManyField("Marks")

# class Subject(models.Model):
#     name = models.CharField(max_length=50)


