from django import forms


class Update_comment(forms.Form):
    """评论表单"""
    commment_content = forms.CharField(label="评论", widget=forms.Textarea)