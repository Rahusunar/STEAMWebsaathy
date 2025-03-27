from django.db import models

# Create your models here.
class blogs(models.Model):
   
    img = models.ImageField(upload_to='photos/')
    topic = models.CharField(max_length=200)
    disc = models.TextField()
    def __str__(self):
     return self.topic
