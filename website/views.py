from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages
# Create your views here.



def index_view(request):
    return render(request, 'website/index.html')

# def contact_view(request):
#     return render(request, 'website/contact.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, ' your message has been sent successfully')
        else:
            messages.add_message(request,messages.ERROR, ' your message did not submited')
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



def about_view(request):
    return render(request, 'website/about.html')

def portfolio_view(request):
    return render(request, 'website/portfolio.html')

def pricing_view(request):
    return render(request, 'website/pricing.html')

def services_view(request):
    return render(request, 'website/services.html')

def testimonials_view(request):
    return render(request, 'website/testimonials.html')




