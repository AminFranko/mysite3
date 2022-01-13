from django.urls import path
from website.views import *

urlpatterns = [
    path('', index_view),
    path('about', about_view),
    path('contact', contact_view),
    path('portfolio-details', portfolio_details_view),
    path('portfolio', portfolio_view),
    path('pricing', pricing_view),
    path('services', services_view),
    path('team', team_view),
    path('testimonials', testimonials_view),
]