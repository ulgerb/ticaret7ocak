from django.shortcuts import render

# Create your views here.


def basketUser(request):
   context = {}
   return render(request, 'basket.html', context)


def loginUser(request):
   context = {}
   return render(request, 'user/login.html', context)


def registerUser(request):
   context = {}
   return render(request, 'user/register.html', context)
