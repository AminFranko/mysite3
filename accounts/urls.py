from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login',views.login_view,name='login'),
    # login
    # path('login',views.logout_view,name='logout'),

    # logout
    path('login',views.signup_view,name='signup')

    # registration/signup

]