from . import views
from django.urls import path
from booking_service.views import booking


urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('', booking, name='booking'),
    path('accounts/', include('allauth.urls')),
]
