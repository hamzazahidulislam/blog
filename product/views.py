
from django.shortcuts import render
from .models import *

def product_price(request,price):
    product = Product.objects.filter(price=price)
    print(product)
    context = {'product':product}
    return render(request,'product/product_price.htm',context)

def product_filter(request,filter):
    category = Category.objects.get(name=filter)
    print(category)
    product = Product.objects.filter(category=category)
    print(product)
    context = {'product':product}
    return render(request,'product/product_filter.htm',context)

def product_detail(request,id):
    product = Product.objects.get(id=id)
    context = {'product_detail':product}
    return render(request,'product/product_detail.htm',context)


def product_list(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {'product':product,'category':category}

from django.shortcuts import render
from .models import *

def product_price(request,price):
    product = Product.objects.filter(price=price)
    print(product)
    context = {'product':product}
    return render(request,'product/product_price.htm',context)

def product_filter(request,filter):
    category = Category.objects.get(name=filter)
    print(category)
    product = Product.objects.filter(category=category)
    print(product)
    context = {'product':product}
    return render(request,'product/product_filter.htm',context)

def product_detail(request,id):
    product = Product.objects.get(id=id)
    context = {'product_detail':product}
    return render(request,'product/product_detail.htm',context)


def product_list(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {'product':product,'category':category}

    return render(request,'product/index.htm',context)