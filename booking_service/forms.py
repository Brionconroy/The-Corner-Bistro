from .models import Reservation
from django import forms


class DateInput(forms.DateInput):
    """This will set the input type variable required for widget
    on UserBookingForm"""
    input_type = 'date'

class UserBookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('first_name',
                  'last_name',
                  'email',
                  'time',
                  'date',
                  'number_of_guests',
                  'special_request_requirments')
        widgets = {
            'date': DateInput(),
            }
                  
