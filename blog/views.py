from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone
from django.db.models import Sum   # 引用求和的方法
# Create your views here.
import markdown
import datetime
from .models import Article, Category, Topic
from read_record.utils import read_record_once_read, get_seven_days_data,\
    get_today_hot_data, get_yesterday_hot_data  # 计数


class IndexView(ListView):
    # model = Article
    context_object_name = 'article_list'
    queryset = Article.objects.filter(has_pub=0)  # 只显示已经发布的文章
    paginate_by = 3
    template_name = 'blog/index.html'


def category_list(request, category_id):
    """栏目列表详情页"""
    category = get_object_or_404(Category, id=category_id)
    article_list = category.article_set.filter(has_pub=0)
    # 分页
    paginator = Paginator(article_list, per_page=2, orphans=1)
    pages = paginator.page_range  # 生成所有页码
    pages_num = paginator.num_pages  # 总页数
    # gd_page = paginator.page(2)  # 调用指定页面的内容
    page = request.GET.get('page')  # 当前页面
    # 当前页并具有处理超出页码范围的状况，页码不是数字返回第一页，超出返回最后一页
    contacts = paginator.get_page(page)
    return render(request, 'blog/category_list.html', locals())


def detail_blog(request, article_id):
    """文章详情页"""
    article = get_object_or_404(Article, id=article_id)

    # markdown编辑器前端显示
    article.content = markdown.markdown(article.content.replace("\r\n", '  \n'), extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',  # 语法高亮
        'markdown.extensions.toc',   # 自动生成目录
    ], safe_mode=True, enable_attributes=False)

    read_cookie_key = read_record_once_read(request, article)

    per_blog = Article.objects.filter(pub_date__gt=article.pub_date, has_pub=0).last()   # 上一篇
    next_blog = Article.objects.filter(pub_date__lt=article.pub_date, has_pub=0).first()  # 下一篇
    response = render(request, 'blog/detail.html', locals())
    response.set_cookie(read_cookie_key, 'true')  # 阅读cookie标记
    return response


def blog_with_dates(request, year, month):
    """文章归档列表页"""
    blog_dates = Article.objects.filter(pub_date__year=year, pub_date__month=month, has_pub=0)  # 以月份归档
    # 分页
    paginator = Paginator(blog_dates, per_page=2, orphans=1)
    pages = paginator.page_range  # 生成所有页码
    pages_num = paginator.num_pages  # 总页数
    gd_page = paginator.page(2)  # 调用指定页面的内容
    page = request.GET.get('page')  # 当前页面
    # 当前页并具有处理超出页码范围的状况，页码不是数字返回第一页，超出返回最后一页
    contacts = paginator.get_page(page)
    return render(request, 'blog/page.html', locals())


def get_seven_days_hot_articles(i):
    """七日阅读统计方法"""
    today = timezone.now().date()
    date = today - datetime.timedelta(days=i)
    article_list = Article.objects.filter(read_details__date__lt=today, read_details__date__gte=date)\
        .values('id', 'title').annotate(read_nums_sum=Sum('read_details__read_nums'))\
        .order_by('-read_nums_sum')
    return article_list[:7]


def read_num_s(request):
    """统计计数显示页面"""
    article_content_type = ContentType.objects.get_for_model(Article)  # 获取文章模型
    dates, read_num_s = get_seven_days_data(article_content_type)

    # 当日热门文章统计显示
    today_hot_data = get_today_hot_data(article_content_type)
    # 昨日热门文章统计显示
    yesterday_hot_data = get_yesterday_hot_data(article_content_type)
    # 七日热门阅读统计显示
    hot_article_for_seven_days = get_seven_days_hot_articles(7)
    # 一个月内热门阅读统计显示
    hot_article_for_month_days = get_seven_days_hot_articles(30)
    return render(request, 'blog/read_nums.html', locals())