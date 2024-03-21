# Create your views here.

from django.http import HttpResponse
from django.urls import reverse, resolve


def index(request):
    route_url = reverse('order:index')
    print("reverse反向解析得到的路由地址:", route_url)
    result = resolve(route_url)
    print("resolve通过路由地址得到路由信息:", result)
    return HttpResponse("订单信息")


def list(request, year, month, day):
    # kwargs = {'year': 2022, 'month': 11, 'day': 11}
    # route_url = reverse('order:list', kwargs=kwargs)   # 字典传参
    args = [year, month, day]  # 列表传参
    route_url = reverse('order:list', args=args)
    print("reverse反向解析得到的路由地址:", route_url)
    result = resolve(route_url)
    print("resolve通过路由地址得到路由信息:", result)
    return HttpResponse("订单列表")
