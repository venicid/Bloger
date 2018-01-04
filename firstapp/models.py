from django.db import models
from faker import Factory
# Create your models here.


class Article(models.Model):
    """博客内容字段"""
    title = models.CharField(null=True, blank=True, max_length=300)  # 文章标题
    content = models.TextField(null=True, blank=True)  # 文章内容
    TAG_CHOICES = (
        ('ai', 'ai'),
        ('python', 'python'),
        ('linux', 'linux'),
        )
    tag = models.CharField(null=True, blank=True, max_length=10, choices=TAG_CHOICES)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """评论字段表"""
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField(null=True, blank=True)
    belong_to = models.ForeignKey(to=Article, related_name='under_comments', null=True, blank=True)
    best_comment = models.BooleanField(default=False)   # 最优评论字段布尔值

    def __str__(self):
        return self.comment

