from django.shortcuts import render, HttpResponse, redirect, reverse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
from .forms import LoginForm, RegisterForm


def login(request):
    """登录方法"""
    if request.method != "POST":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth.login(request, user)  # 利用系统自带的登录方法进行登录
            return redirect(request.GET.get('from', reverse('blog:index')))

    context = {'form':form}
    return render(request, 'account/login.html', context)


def register(request):
    """注册方法"""
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # 创建用户
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            user.save()
            # 登录用户
            user = auth.authenticate(username=cd['username'], email=cd['email'], password=cd['password'])
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('blog:index')))

    context = {'form': form}
    return render(request, 'account/register.html', context)
