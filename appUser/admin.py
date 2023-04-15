from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
   list_display = ('product', "user", "quanity", "total_price" ,"id") 