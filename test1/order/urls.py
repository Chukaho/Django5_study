from django.urls import path

from . import views

app_name = "order"
# 不同app之间多个views文件的名字可能相同，为防止Django索引错文件，定义一下这个那个app的
urlpatterns = [
    path("index/", views.index, name="index"),
    path("list/<int:year>/<int:month>/<int:day>/", views.list, name="list")
]
