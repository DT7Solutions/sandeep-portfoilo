from django.http import JsonResponse
from django.shortcuts import render
from .models import Blog,Contact
from django.core.mail import send_mail

# Create your views here.


def index(request):
    blog_post = Blog.objects.all()

    #contact form
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        email_body = """
                Name:{} 
                Email:{}
                Message:{}
                Smtp mail testing for sandeep portfolio
                """.format(name,email,message)

        send_mail(
            "Testing SMTP",
            email_body,
            "kajasuresh522@gmail.com",
            ["kajasuresh522@gmail.com"],
            fail_silently=False,
        )


        # validations
        errors = {}

        if not name:
            errors['name'] = 'Name field is required.'

        if not email:
            errors['email'] = 'Email field is required.'

        if not message:
            errors['message'] = 'Message field is required.'

        if errors:
             return render(request, 'uifiles/index.html', {'errors': errors, 'name': name, 'email': email, 'message': message})
        

        else:
            oContact = Contact(Name=name, Email=email, Message=message)
            oContact.save()
            return JsonResponse({'success':True})

    return render(request, 'uifiles/index.html',{'blog_post':blog_post})




def blog_details(request,slug):
    blog_post = Blog.objects.get(SlugLink=slug)
    return render(request, 'uifiles/blog-details.html',{'blog_post':blog_post})

