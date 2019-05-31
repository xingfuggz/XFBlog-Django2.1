from django.contrib.contenttypes.models import ContentType
from .models import ReadNum, ReadDetail
from django.utils import timezone
from django.db.models import Sum   # 引用求和的方法
import datetime


def read_record_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        # 总阅读数加1
        # 如果存在则获取，不存在则创建 get_or_create()方法
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        # if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
        #     # 存在记录
        #     readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        # else:
        #     # 不存在对应记录
        #     readnum = ReadNum(content_type=ct, object_id=obj.pk)
        # # 计数加1
        readnum.read_nums += 1
        readnum.save()

        # 当天阅读数加1
        date = timezone.now().date()
        read_detail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        # if ReadDetail.objects.filter(content_type=ct, object_id=obj.pk, date=date).count():
        #     read_detail = ReadDetail.objects.get(content_type=ct, object_id=obj.pk, date=date)
        # else:
        #     read_detail = ReadDetail(content_type=ct, object_id=obj.pk, date=date)
        read_detail.read_nums += 1
        read_detail.save()
    return key


def get_seven_days_data(content_type):
    """用于显示阅读量数据的方法"""
    today = timezone.now().date()
    dates = []
    read_num_s = []
    for i in range(7, 0, -1):
        # timedelta()是计算时间差值的方法，括号内需传入差值所遵从的条件
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        # aggregate()聚合函数方法,求出当天的结果
        result = read_details.aggregate(read_nums_sum=Sum('read_nums'))
        read_num_s.append(result['read_nums_sum'] or 0)
    return dates, read_num_s


def get_today_hot_data(content_type):
    """ 当日热门文章 """
    today = timezone.now().date()  #  获取到当天的数据
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_nums')
    return read_details[:7]


def get_yesterday_hot_data(content_type):
    """昨日热门文章"""
    today = timezone.now().date()  # 获取到当天的数据
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type, date=yesterday).order_by('-read_nums')
    return read_details[:7]



