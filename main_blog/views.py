from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from account.forms import *


def post_detail(request, post_id):
    # post_detail = Post.objects.get(id=post_id)
    post_detail = get_object_or_404(Post, id=post_id)
    # comment = Comment.objects.filter(post=post_detail)
    # comment = post_detail.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_detail
            comment.save()
            return redirect(post_detail)

    context ={
        'post_detail': post_detail,
        'form': form
        # 'comments':comment
    }
    return render(request, 'blog/post_detail.htm', context)


def home(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    context = {
        'post_list': posts,
        'category': category,
    }
    return render(request,'blog/index.htm',context)