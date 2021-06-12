from django.urls import path
from . import views

app_name= 'account'
urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('signup/submit', views.signup_submit, name="signup_submit"),
    path('signup/complete/<token>', views.sign_up_complete, name="signup_complete"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]