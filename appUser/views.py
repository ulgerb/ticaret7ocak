from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *


# Create your views here.


def basketUser(request):
    
    baskets = Basket.objects.filter(user=request.user)
    total = 0
    for i in baskets:
        total += i.total_price
    KDV = round(total * 0.15, 2)
    total = round(total,2) + KDV
    
    
    if request.method == "POST":
        for k,v in request.POST.items():
            if k != "csrfmiddlewaretoken":
                probasket = baskets.get(id=k[8:])
                probasket.quanity = int(v)
                probasket.total_price = int(v) * probasket.product.price
                probasket.save()
            
        return redirect("basketUser")
    
    context = {
        "baskets":baskets,
        "total": total,
        "KDV": KDV,
    }
    return render(request, 'basket.html', context)

def basketDeleteUser(request,id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect("basketUser")


def loginUser(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)  # doğrulama
        # authenticate eğer kullanıcı varsa bilgiler doğruysa bilgileri saklar yoksa None değeri döndürür

        if user is not None:  # user none değilse
            login(request, user)  # giriş yap
            return redirect("/")  # yönlendirme
        else:
            context = {"hata": "Kullanıcı adı veya şifre yanlış!!"}
            return render(request, 'user/login.html', context)

    context = {}
    return render(request, 'user/login.html', context)


def registerUser(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")  # serhat
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # şifrelerin aynı olması, aynı kullanıcı adı olmıcak, aynı email olmıcak, email doğrulaması
        # şifrenin en az 6 karakter olması, büyük harf ve sayı olması
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(
                        email=email, username=username, password=password1, first_name=name)
                    user.save()

                    return redirect("loginUser")
                else:
                    return render(request, 'user/register.html', {"hata": "Email zaten kullanılıyor!"})
            else:
                context = {"hata": "Kullanıcı adı zaten var!"}
                return render(request, 'user/register.html', context)
        else:
            context = {"hata": "Şifreler aynı değil!"}
            return render(request, 'user/register.html', context)

    context = {}
    return render(request, 'user/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect("/")
