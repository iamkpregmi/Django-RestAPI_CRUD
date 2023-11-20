from django.contrib import admin
from .models import *

class mytodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','completed','created_at')

admin.site.register(mytodo,mytodoAdmin)

