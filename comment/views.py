from django.shortcuts import render,redirect, HttpResponse, reverse
from django.contrib.contenttypes.models import ContentType
# Create your views here.
from .models import Comment
from .forms import Update_commentForm


# def update_comment(request):
#     author = request.user
#     comment_text = request.POST['comment_text']
#     content_type = request.POST['content_type']
#     object_id = int(request.POST['object_id'])
#     model_class = ContentType.objects.get(model=content_type).model_class()   # 得到博客类型
#     model_obj = model_class.objects.get(pk=object_id)
#     comment = Comment(author=author, comment_text=comment_text, content_object=model_obj )
#     comment.save()
#     referer = request.META.get('HTTP_REFERER', reverse('blog:index'))
#     return redirect('%s#comment' % referer)


def update_comment(request):
    if request.method != "POST":
        form = Update_commentForm()
    else:
        form = Update_commentForm(data=request.POST)
        form.author = request.user
        form.content_type = request.POST['content_type']