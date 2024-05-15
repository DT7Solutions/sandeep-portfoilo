from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

# class Category(models.Model):
#     CategoryName = models.CharField(max_length=100)
#     Created = models.DateTimeField(default=datetime.now)

#     def __str__(self):
#         return self.CategoryName
    

#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'



class Blog(models.Model):
    Title = models.CharField(max_length=500,default="")
    CreatedAt = models.DateField()
    CreatedName = models.CharField(max_length=100)
    BodyTitle = models.CharField(max_length=200,null=True)
    Body = RichTextField()
    QuoteTitle = models.CharField(max_length=500,null=True)
    QuotedName = models.CharField(max_length=100, null=True)
    QuoteFrom = models.CharField(max_length=50,null=True)
    SlugLink = models.SlugField(max_length=200)
    Image = models.ImageField(upload_to='uploads/')
   

    def __str__(self):
        return self.Title
    

