from django.contrib import admin
from .models import Save_cart

class AdminClass(admin.ModelAdmin):
    list_display = ('token', 'session_cart')
    list_filter = ('token', 'session_cart')
admin.site.register(Save_cart, AdminClass)
