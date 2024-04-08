from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import UserBookingForm
from django.contrib import messages
from .models import Reservation


def index(request):
    return render(request, 'booking_service/index.html')


def base(request):
    return render(request, 'booking_service/base.html')


def menu(request):
    return render(request, 'booking_service/menu.html')


def booking(request):
    form = UserBookingForm()
    if request.method == 'POST':
        form = UserBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.info(request, 'Booking Successfully!')
            return redirect('booking_details')
            pass
    else:
        return render(request, 'booking_service/booking.html', {'form': form})


def booking_details(request):
    bookings = Reservation.objects.all()
    return render(request,
                  'booking_service/booking_details.html',
                  {'bookings': bookings})

def delete_booking(request):
    booking_id = get_object_or_404(Reservation)
    booking_id.delete()
    bookings = Reservation.objects.all()
    return render(request,
                  'booking_service/booking_details.html',
                  {'bookings': bookings})

def edit_booking(request):
    booking_id = get_object_or_404(Reservation)
    edit_form = {
                "edit_form": BookingForm(instance=booking_id)
            }
    return render(request, "booking_service/edit_booking.html", edit_form)