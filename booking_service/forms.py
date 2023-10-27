from .models import Reservation
from django import forms


class UserBookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('first_name',
                  'last_name',
                  'email',
                  'date_and_time',
                  'number_of_guests',
                  'special_request',
                  'special_requirments')
                  
