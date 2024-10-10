from django.contrib import admin

# Register your models here.
from ipad.models import Ipad

class IpadAdmin(admin.ModelAdmin):
    list_display =('id','img','name','dec','price','category')

admin.site.register(Ipad,IpadAdmin)