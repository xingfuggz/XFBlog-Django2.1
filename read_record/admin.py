from django.contrib import admin
from .models import ReadNum, ReadDetail
# Register your models here.


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_nums', 'content_object')


@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('read_nums', 'content_object', 'date')