from django.db import models

from autoslug import AutoSlugField
# Create your models here.
class Laptop(models.Model):
    img =models.FileField(upload_to="laptops/", max_length=250,null=True,default=None)
    name = models.CharField(max_length=100)
    dec = models.TextField()
    price = models.IntegerField()
    category = 'Laptop'
    slug = AutoSlugField(populate_from = 'name' , unique = True,null=True,default=None )

    def __str__(self):
        return self.name