from . import views
from django.urls import path
from booking_service.views import booking, booking_details


urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('', booking, name='booking'),
    path('accounts/', include('allauth.urls')),
    path('booking_details/', booking_details, name='booking_details'),
]
