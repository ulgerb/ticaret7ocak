from django.db import models
from appMy.models import Product
from django.contrib.auth.models import User
# Create your models here.


# SHOP BASKET START ===============================

class Basket(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   image = models.ImageField(("Ürün Resmi"), upload_to="product", max_length=200)
   quanity = models.IntegerField(("Adet"))
   total_price = models.FloatField(("Toplam Fiyat"))

   def __str__(self):
      return self.product.title

# SHOP BASKET END ===============================