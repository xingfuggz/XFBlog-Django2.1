from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone
# Create your models here.


class ReadNum(models.Model):
    """文章阅读计数"""
    read_nums = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class ReadNumExpandMethod:
    def get_read_num(self):
        """返回阅读计数的方法"""
        try:
            ct = ContentType.objects.get_for_model(self)  # 获取模型
            read_num = ReadNum.objects.get(content_type=ct, object_id=self.pk)   # 设置关联模型
            return read_num.read_nums
        except exceptions.ObjectDoesNotExist:
            return 0


class ReadDetail(models.Model):
    read_nums = models.IntegerField(default=0)

    date = models.DateField(default=timezone.now)   # 获取当前时间
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')