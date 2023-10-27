from . import views
from django.urls import path
from booking_service.views import booking


urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('', booking, name='booking'),
    path('accounts/', include('allauth.urls')),
]
