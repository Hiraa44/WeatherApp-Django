from django.db import models

# Create your models here.

class cityname(models.Model):
    city_name = models.CharField(max_length=100)
    temperature= models.CharField(max_length= 50)
    
