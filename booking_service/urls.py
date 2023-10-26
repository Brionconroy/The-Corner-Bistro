from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('booking/', views.booking, name='booking'),
    path('accounts/', include('allauth.urls')),
]
