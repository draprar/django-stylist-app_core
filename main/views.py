from django.shortcuts import render, redirect
from .models import Appointment, Testimonial, GalleryImage


def home(request):
    return render(request, 'main/home.html')


def booking(request):
    if request.method == 'POST':
        Appointment.objects.create(
            client_name=request.POST['name'],
            email=request.POST['email'],
            service=request.POST['service'],
            date=request.POST['date'],
            status='Pending',
        )
        return redirect('home')
    return render(request, 'main/booking.html')


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/gallery.html', {'images': images})


def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'main/testimonials.html', {'testimonials': testimonials, 'range': range(1, 6)})
