from django.shortcuts import render,redirect
from firstapp.models import Article,Comment
from firstapp.form import CommentForm
# Create your views here.


def index(request):
    """主页视图"""
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Article.objects.filter(tag=queryset)  # 找出tag=ai的文章list
    else:
        article_list = Article.objects.all()  # 获取Article表的所有数据

    context = {}
    context['article_list'] = article_list
    return render(request, 'index.html', context)

# def detail(request,page_num):
#     """加载文章，评论视图"""
#     if request.method == 'GET':
#         form = CommentForm   #实例化表单
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)  #提交数据
#         # print(form) for testing
#         if form.is_valid():   #判断表单的数据是否通过验证
#             name = form.cleaned_data['name']
#             comment = form.cleaned_data['comment']
#             a = Article.objects.get(id=page_num)   #查找出该文章对应的id
#             c = Comment(name=name, comment=comment, belong_to=a)    #写评论
#             c.save()   #保存数据库
#             return redirect(to='detail',page_num=page_num)  #重定向本页
#
#     context = {}
#     article = Article.objects.get(id=page_num)  #取出id为1的这篇文章
#     context['article'] = article
#     context['form'] = form
#     print(form)
#     return render(request, 'detail.html', context)


def detail(request,page_num, error_form=None):
    """加载文章，评论视图"""
    form = CommentForm    # 实例化表单

    context = {}
    article = Article.objects.get(id=page_num)  # 取出id为1的这篇文章
    context['article'] = article

    # 加载最优评论
    a_id = Article.objects.get(id=page_num)   # 查找id为1的这个文章
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a_id)   # 返回这个文章的最优评论
    if best_comment:
        context['best_comment'] = best_comment[0]

    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'detail.html', context)


def detail_comment(request,page_num):
    """post提交评论"""
    form = CommentForm(request.POST)  # 提交数据
    print(form)
    if form.is_valid():   # 判断表单的数据是否通过验证
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        a = Article.objects.get(id=page_num)   # 查找出该文章对应的id
        c = Comment(name=name, comment=comment, belong_to=a)    # 写评论
        c.save()   # 保存数据库
    else:
        return detail(request, page_num, error_form=form)

    return redirect(to='detail',page_num=page_num)  # 重定向本页

