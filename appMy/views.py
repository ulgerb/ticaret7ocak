from django.shortcuts import render, redirect
from .models import *
from appUser.models import Basket
from django.db.models import Count, Sum




def index(request):
   context = {}
   return render(request, 'index.html', context)


def About(request):
   context = {}
   return render(request, 'about.html', context)


def Contact(request):
   context = {}
   return render(request, 'contact.html', context)


def shopPage(request):

   products = Product.objects.all()
   # img = ProductImage.objects.values('product').annotate(Count('product'))

   # for i in img:
   #    print(i)
   
   products_img = ProductImage.objects.all()
   products_img2 = []
   img_list = []
   for i in products_img:
      if i.product.title not in img_list:
         img_list.append(i.product.title)
         products_img2.append(i)
   
   context = {
       "products": products,
       "products_img": products_img2,
      #  "img":img
   }
   return render(request, 'shop.html', context)


def Detail(request, id):
   product = Product.objects.get(id=id)
   product_img = ProductImage.objects.filter(product=product)
   comments = Comment.objects.filter(product=product)

   if request.method == "POST":
      button = request.POST.get("button")
      
      if button == "btn-comment":
         star = request.POST.get("star")
         text = request.POST.get("text")
         title = "Başlık"
         
         comm = Comment(star=star, text=text, product=product,title=title, user=request.user )
         comm.save()
         
         stars = 0
         for i in comments:
            stars += i.star
         stars = stars / len(comments) 
         
         product.stars = round(stars,1)
         product.save()
      elif button == "btn-shopadd":
         quanity = int(request.POST.get("quanity"))
         total_price = (product.price) * (quanity)
         basket_product = Basket.objects.filter(user=request.user,product=product)

         if not basket_product.exists():
            basket = Basket(quanity=quanity, total_price=total_price,
                           user=request.user, product=product, image=product_img[0].image)
            basket.save()
         else:
            basket_product = basket_product.get()
            basket_product.quanity += quanity
            basket_product.total_price += total_price
            basket_product.save()
            
      return redirect('/Detail/'+ id +'/')
   
   context = {
      "product":product,
      "product_img": product_img,
      "comments": comments,
   }
   return render(request, 'shop-single.html', context)
