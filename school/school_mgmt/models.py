from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField("enter password", max_length=10)
    
    def __str__(self):
        return self.name
    
class Mac(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField("enter password", max_length=10)
    
    def __str__(self):
        return self.name
    