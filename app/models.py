from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.category_name


class News(models.Model):
    Title = models.CharField(max_length=500,)
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


class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    Title = models.CharField(max_length=500,default=" ")
    CreatedAt = models.DateTimeField(default=datetime.now)
    CreatedName = models.CharField(max_length=100)
    BodyTitle = models.CharField(max_length=200,null=True)
    Body = RichTextField()
    # QuoteTitle = models.CharField(max_length=500,null=True)
    # QuotedName = models.CharField(max_length=100, null=True)
    # QuoteFrom = models.CharField(max_length=50,null=True)
    SlugLink = models.SlugField(max_length=200)
    Image = models.ImageField(upload_to='uploads/')
   

    def __str__(self):
        return self.Title


class Contact(models.Model):
    formtype = (
        ('contact', 'contact'),
        ('invite', 'invite'),
    )

    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Message = models.TextField()
    Form_type = models.CharField(choices=formtype, max_length=30, default='contact')
    SearchFields = ['Name','Email','Message']
  


    def __str__(self):
        return self.Name
    





class PortfolioPopupSubmit(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    

class NewsletterSubscription(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    invite_email = models.EmailField()
    city = models.CharField(max_length=100)
    looking_for = models.TextField()  # Store selected checkboxes as a comma-separated string
    other_problem = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
