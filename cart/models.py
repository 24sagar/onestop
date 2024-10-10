from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_slug = models.SlugField(default='', null= False)
    product_category = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product_category} - {self.product_slug} (x{self.quantity})"

class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.address}"