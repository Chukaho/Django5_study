"""
URL configuration for test1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

'''
include函数：用于在主URL配置文件中包含应用程序的 URL 配置文件。
这样的组织结构使得项目的URL配置更加模块化和可维护，有助于更清晰地组织和管理不同应用程序的 URL 结构。
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', admin.site.urls),
    path('redirectTo/', RedirectView.as_view(url="index/")),  # 重新定向跳转到index页面
    path('helloworld/', include(("helloworld.urls"), namespace='helloworld')),
    # 空间命名法只提供了前缀，后面还要索引到具体的app里面的urls文件路径，仅输入空间标签无法访问
    path('order/', include(("order.urls"), namespace='order')),
    path('user/', include(("user.urls"), namespace='user')),
]
