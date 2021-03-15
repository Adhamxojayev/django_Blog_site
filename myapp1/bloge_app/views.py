from django.shortcuts import render
from django.http import HttpResponse
from .models import PostYoz

def index1(request):
    post_list = PostYoz.objects.all()
    return render(request,"blog_fayllari/index.html",{"blog_list":post_list[::-1]})

def qalesan(request):
    return render(request,"blog_fayllari/qalesan.html")










