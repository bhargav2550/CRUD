from django.db import models

# Create your models here.
class student(models.Model):
    FirstName = models.CharField(max_length=20)
    #LastName = models.CharField(max_length=20)
    TestScore = models.FloatField()

class course(models.Model):
    name = models.CharField(max_length=10)
    description=models.TextField()
    instructor = models.CharField(max_length=10)
    rating = models.IntegerField()
