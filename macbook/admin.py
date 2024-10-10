from django.contrib import admin
from macbook.models import Macbook

class MacbookAdmin(admin.ModelAdmin):
    list_display =('id','img','name','dec','price','category')

admin.site.register(Macbook,MacbookAdmin)
# Register your models here.
