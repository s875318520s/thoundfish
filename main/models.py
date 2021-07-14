from django.db import models


# Create your models here.
class unit(models.Model):
    index = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='顯示名稱')
    status_1 = models.BooleanField(default=False, verbose_name='狀態一')
    status_2 = models.BooleanField(default=False, verbose_name='狀態二')
    status_1_change = models.DateTimeField(null=True, blank=True, verbose_name='狀態一修改時間')
    status_2_change = models.DateTimeField(null=True, blank=True, verbose_name='狀態二修改時間')
    status_1_uesr = models.CharField(max_length=10, null=True, blank=True, verbose_name='狀態一修改人')
    status_2_uesr = models.CharField(max_length=10, null=True, blank=True, verbose_name='狀態二修改人')
