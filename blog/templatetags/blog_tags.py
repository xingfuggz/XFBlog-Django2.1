from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from blog.models import Article, Category


register = template.Library()


@register.simple_tag
def archives():
    """文章归档"""
    return Article.objects.dates('pub_date', 'month', order='DESC')


@register.simple_tag
def archives_num(year, month):
    """文章归档按月份统计数量"""
    return Article.objects.filter(pub_date__year=year, pub_date__month=month, has_pub=0).count()


@register.simple_tag
def get_categorys():
    """分类目录"""
    return Category.objects.all()


@register.simple_tag
def get_articel_nums(category_id):
    """统计每个分类下的文章数量"""
    category = get_object_or_404(Category, id=category_id)
    return category.article_set.filter(has_pub=0).count()
