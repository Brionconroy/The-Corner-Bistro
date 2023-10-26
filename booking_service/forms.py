from django.views.generic import CreateView
from .models import Reservation


class UserBookingForm(CreateView):
    class Meta:
        model = Reservation
        fields = ('first_name',
                  'last_name',
                  'email',
                  'date_and_time',
                  'number_of_guests',
                  'special_request',
                  'special_requirments')
