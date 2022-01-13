from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view,name='about'),
    path('contact', contact_view,name='contact'),
    path('portfolio-details', portfolio_details_view,name='portfolio-details'),
    path('portfolio', portfolio_view,name='portfolio'),
    path('pricing', pricing_view,name='pricing'),
    path('services', services_view,name='services'),
    path('team', team_view,name='team'),
    path('testimonials', testimonials_view,name='testimonials'),
]