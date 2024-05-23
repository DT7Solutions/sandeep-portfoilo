from django.contrib import admin
from .models import Blog,Contact

# Register your models here.


class AdminBlog(admin.ModelAdmin):
    list_display = ['Title','CreatedAt','Image','BodyTitle']



class AdminContact(admin.ModelAdmin):
    list_display = ['Name','Email','Message']
    list_filter = ['Name']
    search_fields = Contact.SearchFields




admin.site.register(Blog,AdminBlog)
admin.site.register(Contact,AdminContact)