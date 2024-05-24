from django.contrib import admin
from django.http import HttpResponse
from .models import Blog,Contact
import csv

# Register your models here.


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
    



admin.site.register(Blog,AdminBlog)
admin.site.register(Contact,AdminContact)