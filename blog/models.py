from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
# Create your models here.
from read_record.models import ReadNum, ReadDetail, ReadNumExpandMethod


class Category(models.Model):
    """博客分类"""
    name = models.CharField('分类名称', max_length=32)
    slug = models.SlugField('slug', max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    desc = models.TextField('分类描述', max_length=200)
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "博客分类"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """文章标签"""
    name = models.CharField('标签', max_length=20)
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "标签管理"

    def __str__(self):
        return self.name


class Article(models.Model, ReadNumExpandMethod):
    """文章管理"""
    HAS_PUB_CHOICES = (
        (0, '发布'),
        (1, '存草稿'),
    )
    HAS_REPRINT_CHOICES = (
        (0, '原创'),
        (1, '转载'),
    )

    title = models.CharField('文章标题', max_length=100)
    slug = models.SlugField('slug', max_length=100, blank=True, null=True, help_text="链接后缀，必须为英文字符")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    read_details = GenericRelation(ReadDetail)  # 关联到这个模型，可以很方便的访问关联模型的所有数据
    desc = models.TextField(max_length=100, blank=True, help_text="文章简介，字数保持在100以内！")
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, verbose_name="专题", blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="分类")
    picture = models.ImageField('封面图', upload_to='images/', max_length=200, blank=True, null=True)
    content = MDTextField()
    tags = models.ManyToManyField('Tag', blank=True)
    has_pub = models.PositiveSmallIntegerField('是否发布',choices=HAS_PUB_CHOICES, default=0)
    has_reprint = models.PositiveSmallIntegerField('是否原创', choices=HAS_REPRINT_CHOICES, default=0)
    has_url = models.URLField('原文链接', blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "文章管理"

    def __str__(self):
        return self.title


class Topic(models.Model):
    """专题管理"""
    name = models.CharField('专题名称', max_length=200)
    slug = models.SlugField('slug', max_length=100)
    desc = models.TextField('专题描述', max_length=300, blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "专题管理"

    def __str__(self):
        return self.name
        
        
# class ReadNum(models.Model):
#     """文章阅读计数"""
#     read_nums = models.IntegerField(default=0)
#     article = models.OneToOneField(Article, on_delete=models.DO_NOTHING)
