from django.db import models
from django.contrib.auth.models import User



# PRODUCT START ===============================
class ProductColor(models.Model):
   title = models.CharField(("Renk"), max_length=50)
   
   def __str__(self):
      return self.title

class Product(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Açıklama"))
   price = models.FloatField(("Fiyat"))
   stok = models.IntegerField(("Stok"))
   colors = models.ManyToManyField(ProductColor, verbose_name=("Ürün Renkleri"))
   stars = models.FloatField(("Ürün Puanı"), default=0)
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   
   def __str__(self):
      return self.title
   
class ProductImage(models.Model):
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   image = models.ImageField(("Ürün Resmi"), upload_to='product',  max_length=200)
   
   def __str__(self):
      return self.product.title

# PRODUCT END ===============================

# COMMENT START ===============================

class Comment(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   title = models.CharField(("Konu"), max_length=50)
   text = models.TextField(("Yorum"))
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   star = models.IntegerField(("Yıldız"), default=5)
   
   
   def __str__(self):
      return self.product.title

# COMMENT END ===============================



