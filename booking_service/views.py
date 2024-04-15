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
            booking.user_id = request.user.id
            booking.save()
            return redirect('booking_details')
    else:
        return render(request, 'booking_service/booking.html', {'form': form})


def booking_details(request):
    bookings = Reservation.objects.all().filter(user_id=request.user.id)
    return render(request,
                  'booking_service/booking_details.html',
                  {'bookings': bookings})

def delete_booking(request, naming_id):
    booking = get_object_or_404(Reservation, naming_id=naming_id)
    booking.delete()
    return redirect('booking_details')


def edit_booking(request, naming_id):
    booking = get_object_or_404(Reservation, naming_id = naming_id)
    edit_form = {
                "edit_form": UserBookingForm(instance=booking)
            }
    if request.method == 'POST':
        form = UserBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user_id = request.user.id
            booking.naming_id = naming_id
            booking.save()
            return redirect('booking_details')
    else:
        return render(request, "booking_service/edit_booking.html", edit_form)