from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

   list_display = ('title','price', 'user', "stok", "stars", "id")
   list_filter = ('date_now',)
   search_fields = ('title', 'user', 'text', 'stars')
   date_hierarchy = 'date_now'
   ordering = ('-id',)


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
   list_display = ('title', "id")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
   list_display = ('product', "id")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
   list_display = ('product', "user", "star" ,"id") 