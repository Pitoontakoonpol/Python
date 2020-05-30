from django.urls import path
from .views import homePage, aboutPage, contactUs

urlpatterns = [
    path('',homePage, name='home-page'),
    path('about/', aboutPage,name='about-page'),
    path('contact/', contactUs,name='contact-page')
]
