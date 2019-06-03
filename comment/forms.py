from django import forms
from .models import Comment

# class Update_comment(forms.Form):
#     """评论表单"""
#     commment_content = forms.CharField(label="评论", widget=forms.Textarea)


class Update_commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

