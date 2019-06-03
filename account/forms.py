from django import forms
from django.contrib import auth
from django.shortcuts import redirect, reverse


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(label='用户名', max_length=32)
    password = forms.CharField(label='密码', widget=forms.PasswordInput, max_length=16)

    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     user = auth.authenticate(username=username, password=password)
    #     if user is not None:
    #         raise forms.ValidationError('用户名或密码错误')
    #     else:
    #         self.cleaned_data['user'] = user
    #     return self.cleaned_data


