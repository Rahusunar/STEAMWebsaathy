from django.db import models

# Create your models here.
class kit(models.Model):
    level = models.TextField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=False, blank=False)
    discount = models.FloatField(null=True, blank=True, default=0.0)
    image = models.ImageField(upload_to='photos/')
    disc  = models.TextField();
    def __str__(self):
        return self.name