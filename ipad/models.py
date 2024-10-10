from django.db import models
from autoslug import AutoSlugField

class Ipad(models.Model):
    img = models.FileField(upload_to="ipads/", max_length=250, null=True, default=None)
    name = models.CharField(max_length=100)
    dec = models.TextField()
    price = models.IntegerField()
    category = "Ipad"
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)

    def __str__(self):
        return self.name


