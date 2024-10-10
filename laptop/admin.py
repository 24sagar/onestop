from django.contrib import admin

# Register your models here.
from laptop.models import Laptop

class LaptopAdmin(admin.ModelAdmin):
    list_display =('id','img','name','dec','price','category')

admin.site.register(Laptop,LaptopAdmin)