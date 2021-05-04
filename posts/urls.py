from django.urls import path
from .views import main_page, about, gallery, contact


urlpatterns = [
    path('', main_page, name='main_page'),
    path('about/', about, name='about' ),
    path('contact/', contact, name='contact'),
    path('gallery', gallery, name='gallery')
]