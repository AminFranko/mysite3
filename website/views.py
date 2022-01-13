from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.



def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def about_view(request):
    return render(request, 'website/about.html')

def portfolio_details_view(request):
    return render(request, 'website/portfolio-details.html')

def portfolio_view(request):
    return render(request, 'website/portfolio.html')

def pricing_view(request):
    return render(request, 'website/pricing.html')

def services_view(request):
    return render(request, 'website/services.html')

def team_view(request):
    return render(request, 'website/team.html')

def testimonials_view(request):
    return render(request, 'website/testimonials.html')




