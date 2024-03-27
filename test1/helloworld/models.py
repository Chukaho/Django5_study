from django.db import models


# Create your models here.
class StudentInfo(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField自动分配一个递增的整数值作为字段的值。
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = "t_student"
