from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
# Create your views here.
from .forms import LoginForm


def login(request):
    if request.method != "POST":
        form = LoginForm()
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog:index')
        else:
            return HttpResponse("登录不成功，请检查用户名密码是否正确")
    context = {'form': form}
    return render(request, 'account/login.html', context)
