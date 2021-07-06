from django.contrib import admin
from .models import Product

class AdminClass(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image',)
    list_filter = ('name', 'price',)
admin.site.register(Product, AdminClass)
