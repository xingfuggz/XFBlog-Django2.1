from django import forms


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(label='用户名', max_length=32)
    password = forms.CharField(label='密码', widget=forms.PasswordInput, max_length=16)


