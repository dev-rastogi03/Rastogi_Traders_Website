from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('offers/', views.OffersView.as_view(), name='offers'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('privacy-policy/', views.PrivacyPolicyView.as_view(), name='privacy'),
    path('terms-and-conditions/', views.TermsConditionsView.as_view(), name='terms'),
    path('cookies-policy/', views.CookiesPolicyView.as_view(), name='cookies'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]
