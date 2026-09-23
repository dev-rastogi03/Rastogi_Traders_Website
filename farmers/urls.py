from django.urls import path
from . import views

app_name = 'farmers'

urlpatterns = [
    path('', views.FarmerCornerIndexView.as_view(), name='index'),
    path('crop/<str:slug>/', views.CropGuideDetailView.as_view(), name='crop_detail'),
    path('tips/<str:slug>/', views.FarmerTipDetailView.as_view(), name='tip_detail'),
]
