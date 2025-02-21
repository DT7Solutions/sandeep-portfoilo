
from django.urls import path
from .views import index,blog,blog_details,news_details,submit_form,save_newsletter_subscription



urlpatterns = [
    path('',index, name='index'),
    path('blog-grid/',blog,name="blog-grid"),
    path('news-details/<slug:slug>/',news_details,name='news_details'),
    path('blog-details/<slug:slug>/',blog_details,name='blog_details'),
    path('submit-form/',submit_form, name="submit-form"),
    path('save-newsletter/', save_newsletter_subscription, name='save_newsletter'),
]

