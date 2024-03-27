from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
'''
    Flight.objects.all(): 这是一个查询集（QuerySet），表示从数据库中检索所有的 Flight 对象。
    Flight 是一个模型
    objects 是 Django 自动生成的一个管理器（Manager），它提供了一些用于查询数据库的方法。
    all() 是其中的一个方法，它返回模型中的所有对象。
'''


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


'''
.exclude(flight=flight): 这是一个查询过滤器，它指示排除那些与给定 flight 对象相关联的 Passenger 对象。
具体来说，它从 Passenger 模型中排除那些 flight 外键字段与给定的 flight 对象不匹配的记录。

.all(): 这表示获取所有符合前面条件的结果。在这里，它告诉 Django 返回符合排除条件的所有 Passenger 对象。
flight=flight 中的第一个 flight 是字段名，它指代了 Passenger 模型中与航班相关的外键字段，
而第二个 flight 是变量名，它代表了一个特定的航班对象。
'''


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
