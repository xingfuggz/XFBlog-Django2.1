from django.db import models
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from .models import Comment



class CKEditorWidget(forms.Textarea):
    class Media:
        js = (
            'ckeditor5/ckeditor.js',
            'ckeditor5/config.js',
            'ckeditor5/translations/zh.js',
            'ckeditor5/translations/zh-cn.js'
        )


class CommentForm(forms.Form):
    content_type = forms.CharField(label="要评论的模型", widget=forms.HiddenInput)
    object_id = forms.IntegerField(label="获取到要使用模型的id", widget=forms.HiddenInput)
    comment_text = forms.CharField(label="评论内容", widget=forms.Textarea(attrs={
        'class': 'textarea is-radiusless is-shadowless',
    }))
    # comment_text = forms.CharField(label="评论内容", widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')

        # 评论对象验证
        content_type = self.cleaned_data['content_type']  # 获取所有模型名称
        object_id = self.cleaned_data['object_id']  # 模型id
        # 获取当前模型名称，并用model_class()方法返回首字母大写
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(id=object_id)
            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论对象不存在')
        return self.cleaned_data



