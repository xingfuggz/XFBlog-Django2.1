from django.shortcuts import render, HttpResponse, redirect, reverse, HttpResponseRedirect
from django.contrib import auth
# Create your views here.
from .forms import LoginForm


def login(request):
    if request.method != "POST":
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        if form.is_valid():
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(request.GET.get('from', reverse('blog:index')))
            else:
                form.add_error(None, '用户名或密码错误')
                return render(request, 'account/login.html', {'form':form})
        else:
            return HttpResponse('你填写的用户名密码类型错误')
    context = {'form': form}
    return render(request, 'account/login.html', context)

