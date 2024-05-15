
from django.urls import path
from .views import index,blog_details



urlpatterns = [
    path('',index, name='index'),
    path('blog-details/<slug:slug>/',blog_details,name='blog_details'),
]
