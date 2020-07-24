from django.shortcuts import render
from .models import *


def post_detail(request, post_id):
    post_detail = Post.objects.get(id=post_id)
    context ={
        'post_detail': post_detail
    }
    return render(request,'blog/post_detail.htm',context)


def home(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    context = {
        'post_list': posts,
        'category': category,
    }
    return render(request,'blog/index.htm',context)