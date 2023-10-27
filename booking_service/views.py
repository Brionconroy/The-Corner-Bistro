from django.shortcuts import render
from .forms import UserBookingForm


def index(request):
    return render(request, 'booking_service/index.html')


def base(request):
    return render(request, 'booking_service/base.html')


def booking(request):
    form = UserBookingForm()
    if request.method == 'POST':
        form = UserBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.info(request, 'Booking Successfully!')
            pass
    else:

        return render(request, 'booking_service/booking.html', {'form': form})
