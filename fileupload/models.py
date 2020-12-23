from django.db import models

# Create your models here.
class Imgmanager(models.Model):    
    image_name = models.CharField(max_length=100)    
    image = models.ImageField(default='media/default_image.jpeg') # null=True