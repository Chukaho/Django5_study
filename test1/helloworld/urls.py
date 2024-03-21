from django.urls import path, re_path

from . import views

app_name = "helloworld"
# 不同app之间多个views文件的名字可能相同，为防止Django索引错文件，定义一下这个那个app的
urlpatterns = [
    path("index/", views.index, name="index"),
    path("blog/<int:id>", views.blog, name="blog"),
    re_path(r'^blog2/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.blog2, name="blog2"),
    path("download/", views.download, name="download"),
    path("st_download/", views.st_download, name="st_download"),
    path("file_download/", views.file_download, name="file_download"),
    path("get/", views.get_test, name="get_test"),
    path("post", views.post_test, name="post_test"),
    path('tologin', views.to_login, name="to_login"),
    path('login', views.login, name="login"),
    path('toupload', views.to_upload, name="to_upload"),
    path('upload', views.upload, name="upload"),
]
