from django.db import models

# Create your models here.

class types(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to='profile')

class newtypes(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='profile')
    desc=models.TextField()
