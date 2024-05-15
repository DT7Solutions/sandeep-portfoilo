from django.contrib import admin
from .models import Blog

# Register your models here.

class AdminBlog(admin.ModelAdmin):
    list_display = ['Title','CreatedAt','Image','BodyTitle']





admin.site.register(Blog,AdminBlog)