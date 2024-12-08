from django.urls import path
from . import views
from .views import contact_view
urlpatterns = [
    path('', views.home, name='home'),
    path('fine_details/', views.fine_details, name='fine_details'),
    path('expiry_details/', views.expiry_details, name='expiry_details'),
    path('contact_us/', views.contact_view, name='contact_us'),
    path('search_license/', views.search_license, name='search_license'),
    
  
]
