from .models import Reservation
from django import forms
from .widget import DatePickerInput, TimePickerInput


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
            'date': DatePickerInput(),
            'time' : TimePickerInput(),
            }
                  
