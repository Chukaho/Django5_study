from django.db import models


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    '''
    models.ForeignKey: 这是一个字段类型，表示数据库中的外键关系,说明引用了另外的类。
    CASCADE: 意味着当与此外键相关联的Airport对象被删除时，将删除所有与之关联的对象。
    related_name="departures": 这是可选的，它定义了从关联模型反向访问，自由命名反向名称。
    '''
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"  # Django自动添加序号到SQL表中


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"


'''
models.ManyToManyField: 这是 Django 模型字段的类型，表示多对多关系。这种类型的字段允许一个对象和多个其他对象之间的多对多关联。
blank=True: 这表示字段在表单中可以为空。这意味着用户可以不必选择该字段的值，即该字段可以为空。
'''
