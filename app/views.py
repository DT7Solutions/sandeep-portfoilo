from django.http import JsonResponse
from django.shortcuts import render
from .models import Blog,News,Contact,PortfolioPopupSubmit
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.


def index(request):
    blog_post = Blog.objects.filter().order_by("-id")[:3]
    news_post = News.objects.all()
    

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
            name,
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

        # if not full_name :
        #     errors['full_name'] = 'Name field is required.' 
        
        # if not invite_email :
        #     errors['full_name'] = 'Name field is required.' 
        
        # if not reach_message :
        #     errors['full_name'] = 'Name field is required.' 

        if errors:
             return render(request, 'uifiles/index.html', {'errors': errors, 'name': name, 'email': email, 'message': message,})
        

        else:
            oContact = Contact(Name=name, Email=email, Message=message,Form_type=form_type)
            oContact.save()
            return JsonResponse({'success':True})

    return render(request, 'uifiles/index.html',{'blog_post':blog_post, 'news_post':news_post})

def blog(request):
    blog_items = Blog.objects.filter().order_by("-id")  # Assuming you retrieve all blog items from your model
    
    paginator = Paginator(blog_items, 6)  # Show 6 blog items per page

    page_number = request.GET.get('page')
    try:
        blog_page = paginator.page(page_number)
    except PageNotAnInteger:
        blog_page = paginator.page(1)
    except EmptyPage:
        blog_page = paginator.page(paginator.num_pages)

    context = {
        'blog_item': blog_page,  # Pass the paginated page object to the template
        'post': blog_page,  # This is used in your template for pagination checking
    }

    return render(request, 'uifiles/blog.html', context)


def news_details(request,slug):
    news_post = News.objects.get(SlugLink=slug)
    return render(request, 'uifiles/news-details.html',{'news_post':news_post})


def blog_details(request,slug):
    blog_post = Blog.objects.get(SlugLink=slug)
    return render(request, 'uifiles/blog-details.html',{'blog_post':blog_post})



@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        popname = request.POST.get('popname')
        popemail = request.POST.get('popemail')
        popphone = request.POST.get('popphone')
        popcity = request.POST.get('popcity')

        # Save the data to the database
        portfolio_submission = PortfolioPopupSubmit(
            name=popname,
            email=popemail,
            phone=popphone,
            city=popcity
        )
        portfolio_submission.save()

        # Send an email
        send_mail(
            subject="Portfolio Form Submission",
            message=f"Name: {popname}\nEmail: {popemail}\nPhone: {popphone}\nCity: {popcity}",
            from_email="connectmagsmen@gmail.com",
            recipient_list=['kajasuresh522@gmail.com'],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Portfolio submitted successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)