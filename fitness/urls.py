
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('enroll', views.enroll, name='enroll'),
    path('contact', views.contact, name='contact')
]
