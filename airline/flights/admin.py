from django.contrib import admin
from .models import Flight, Airport, Passenger


# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")  # 管理页面显示的内容


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)  # filter_horizontal 方法添加水平选择框


admin.site.register(Airport)  # 告诉管理员程序控制这两个对象
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
