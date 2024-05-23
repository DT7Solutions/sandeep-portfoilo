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
        full_name = request.POST.get('full_name')
        invite_email = request.POST.get('invite_email')
        reach_message = request.POST.get('message')
        form_type = request.POST.get('form_type')

        email_body = """
                Name:{} 
                Email:{}
                Message:{}
                """.format(name,email,message)

        send_mail(
            email_body,
            "noreplayitsnsandeep@gmail.com",
            ["admin@itsnsandeep.com"],
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

        if not full_name :
            errors['full_name'] = 'Name field is required.' 
        
        if not invite_email :
            errors['full_name'] = 'Name field is required.' 
        
        if not reach_message :
            errors['full_name'] = 'Name field is required.' 

        if errors:
             return render(request, 'uifiles/index.html', {'errors': errors, 'name': name, 'email': email, 'message': message, 'full_name':full_name,'invite_email':invite_email,'reach_message':reach_message})
        

        else:
            oContact = Contact(Name=name, Email=email, Message=message,Form_type=form_type)
            oContact.save()
            return JsonResponse({'success':True})

    return render(request, 'uifiles/index.html',{'blog_post':blog_post})




def blog_details(request,slug):
    blog_post = Blog.objects.get(SlugLink=slug)
    return render(request, 'uifiles/blog-details.html',{'blog_post':blog_post})

