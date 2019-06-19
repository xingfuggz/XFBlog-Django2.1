from django.shortcuts import render,redirect, HttpResponse, reverse
from django.contrib.contenttypes.models import ContentType
# Create your views here.
from .models import Comment
from .forms import CommentForm


def update_comment(request):
    # 这里的request.user是在forms集成表单初始化过的数据
    form = CommentForm(request.POST, user=request.user)
    if form.is_valid():
        # 检查通过保存数据
        cd = form.cleaned_data
        comment = Comment(author=request.user, comment_text=cd['comment_text'], content_object=cd['content_object'])
        comment.save()

        referer = request.META.get('HTTP_REFERER', reverse('blog:index'))
        return redirect('%s#comment' % referer)
    else:
        return render(request, 'comment/error.html', {'message': form.errors})

