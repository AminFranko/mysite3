from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view,name='about'),
    path('contact', contact_view,name='contact'),
    path('portfolio', portfolio_view,name='portfolio'),
    path('pricing', pricing_view,name='pricing'),
    path('services', services_view,name='services'),
    path('testimonials', testimonials_view,name='testimonials'),
    path('newsletter',newsletter_view,name='newsletter')
]