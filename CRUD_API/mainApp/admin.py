from django.contrib import admin
from .models import *

# Product admin and their visible fields
class productsAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','price','quantity')

admin.site.register(products,productsAdmin)


