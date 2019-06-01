from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    """创建的评论对象"""
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)   # 关联模型
    object_id = models.PositiveIntegerField()   # 模型id
    content_object = GenericForeignKey('content_type', 'object_id')  #  关联模型和模型id

    comment_text = models.TextField('评论内容')
    comment_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-comment_time']
        verbose_name_plural = "评论"

    def __str__(self):
        return self.comment_text
