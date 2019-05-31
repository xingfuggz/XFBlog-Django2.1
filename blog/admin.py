from django.contrib import admin

# Register your models here.
from .models import Category, Article, Topic, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'add_date', 'pub_date')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','topic', 'category', 'get_read_num', 'has_pub', 'has_reprint', 'add_date', 'pub_date')
    list_editable = ('has_pub', 'has_reprint')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date', 'pub_date')


@admin.register(Tag)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date', 'pub_date')


# @admin.register(ReadNum)
# class ReadNumAdmin(admin.ModelAdmin):
#     list_display = ('article', 'read_nums')
