from django.shortcuts import render

# Create your views here.


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
   context = {}
   return render(request, 'shop.html', context)


def Detail(request):
   context = {}
   return render(request, 'shop-single.html', context)
