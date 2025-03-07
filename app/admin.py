from django.contrib import admin
from django.http import HttpResponse
from .models import Blog,News,Contact,Category,PortfolioPopupSubmit,NewsletterSubscription
import csv

# Register your models here.

# class AdminCategory(admin.ModelAdmin):
#      list_display = ['Category_name']


class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']


class AdminNews(admin.ModelAdmin):
    list_display = ['Title','CreatedAt','Image','BodyTitle']


class AdminBlog(admin.ModelAdmin):
    list_display = ['Title','CreatedAt','Image','BodyTitle']



class AdminContact(admin.ModelAdmin):
    list_display = ['Name','Email','Message','Form_type']
    list_filter = ['Form_type']

    actions = ['export_to_csv']
    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
             writer.writerow([getattr(obj, field) for field in fieldnames])
        return response
    export_to_csv.short_description = "Download selected as csv"
    

class AdminPortfolioPopupSubmit(admin.ModelAdmin):
    list_display = ['name','email','phone','city']


class AdminNewsletter(admin.ModelAdmin):
    list_display = ['full_name','phone_number','invite_email','city','looking_for','other_problem']


admin.site.register(Category,AdminCategory)
admin.site.register(News,AdminNews)
admin.site.register(Blog,AdminBlog)
admin.site.register(Contact,AdminContact)
admin.site.register(PortfolioPopupSubmit,AdminPortfolioPopupSubmit)
admin.site.register(NewsletterSubscription,AdminNewsletter)