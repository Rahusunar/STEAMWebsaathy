from django.db import models

class CodingClassEnrollment(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)  # You may adjust the length as needed
    course_level = models.CharField(max_length=50, choices=[
        ('basic', 'Basic Level of Coding'),
        ('advanced', 'Advanced Level of Coding'),
        ('basic-advance', 'Basic to Advance Level of Coding'),
    ])

    def __str__(self):
        return f"{self.name} - {self.course_level}"

class exploreKits(models.Model):
    kit_name = models.CharField(max_length=100)
    Img = models.ImageField(upload_to="photot/")
    starting_price = models.FloatField()
    Ending_price = models.FloatField()
    about_kit = models.TextField()
    
    def __str__(self):
        return f"{self.kit_name}, {self.starting_price}-{self.Ending_price}"


class Category(models.Model):
    img = models.ImageField(upload_to='category_photot/')
    name= models.CharField( max_length=100)
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    img = models.ImageField(upload_to='product_img/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
