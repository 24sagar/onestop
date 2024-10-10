from django.contrib import admin
from iphone.models import Iphone

class IphoneAdmin(admin.ModelAdmin):
    list_display =('id','img','name','dec','price','category')

admin.site.register(Iphone,IphoneAdmin)

# Register your models here.
