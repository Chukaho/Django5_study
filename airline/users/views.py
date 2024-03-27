from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request) -> bool:
    if request.user.is_authenticated:
        # .is_authenticated 是一个属性，它返回一个布尔值，指示用户是否已经通过身份验证。
        # 如果用户已经登录，则该属性返回 True，否则返回 False。
        return render(request, "users/user.html")
    return HttpResponseRedirect(reverse("login_view"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)  # Django自带的验证方法
        if user is not None:
            login(request, user)  # Django自带的方法
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)  # Django自带的方法
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
