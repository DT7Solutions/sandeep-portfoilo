from django.shortcuts import render
from .models import Blog

# Create your views here.


def index(request):
    blog_post = Blog.objects.all()
    return render(request, 'uifiles/index.html',{'blog_post':blog_post})

def blog_details(request,slug):
    blog_post = Blog.objects.get(SlugLink=slug)
    return render(request, 'uifiles/blog-details.html',{'blog_post':blog_post})

