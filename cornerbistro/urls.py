from django.contrib import admin
from django.urls import path, include
from booking_service import views
from booking_service.views import booking, booking_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('accounts/', include('allauth.urls')),
    path('booking/', booking, name='booking'),
    path('menu/', views.menu, name='menu'),
    path('booking_details/', booking_details, name='booking_details'),
]
