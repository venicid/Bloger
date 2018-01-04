from django import forms
from django.core.exceptions import ValidationError


def words_validator(comment):
    """验证器函数"""
    if len(comment) < 5:
        raise ValidationError('内容长度不足5个字符')

def comment_validator(comment):
    """过滤器"""
    if '?' in comment:
        raise ValidationError('不能包含这个字符')

class CommentForm(forms.Form):
    """定义Django自带的form表单"""
    name = forms.CharField(max_length=50,
                           error_messages={
                               'required': '请输入内容',
                                },
                           )

    comment = forms.CharField(              # 修改表单样式
        widget=forms.Textarea,
        error_messages={
            'required':'请输入内容',
            },
        validators=[words_validator,comment_validator]
        )
