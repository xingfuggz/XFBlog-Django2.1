from django import forms
from django.contrib import auth
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(label='用户名', max_length=32,
                               widget=forms.TextInput(
                                    attrs={
                                        'class': 'input',
                                        'placeholder': '请输入用户名',
                                    }))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'input',
                                       'placeholder': '请输入长度小于16位密码',
                                   }), max_length=16)

    def clean(self):
        db = self.cleaned_data
        username = db['username']
        password = db['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:  # 如果用户名密码为空或者错误
            # 主动触发报错信息
            raise forms.ValidationError('用户名或密码错误')
        else:
            # 把user的传入数组
            db['user'] = user
        return db


class RegisterForm(forms.Form):
    """注册表单"""
    username = forms.CharField(label='用户名', widget=forms.TextInput(
                                attrs={
                                    'class': 'input',
                                    'placeholder': '请输入用户名'
                                }), max_length=32,min_length=3,)

    email = forms.EmailField(label='邮箱', widget=forms.EmailInput(
                                attrs={
                                    'class': 'input',
                                    'placeholder': '请输入正确的邮箱地址',
                                }))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(
                                attrs={
                                    'class': 'input',
                                    'placeholder': '请输入长度小于16位密码',
                                }), max_length=16, min_length=6)
    password1 = forms.CharField(label='再次输入密码', widget=forms.PasswordInput(
                                attrs={
                                    'class': 'input',
                                    'placeholder': '再输入一次密码',
                                }), max_length=16, min_length=6)

    def clean_username(self):
        """验证用户名是否已被注册"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        """验证邮箱"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱地址已被注册')
        return email

    def clean_password1(self):
        """验证两次密码是否一致"""
        cd = self.cleaned_data
        if cd['password'] != cd['password1']:
            raise forms.ValidationError('您输入的两次密码不一致')
        return cd['password1']

