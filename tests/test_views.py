import pytest
from django.urls import reverse
from main.models import Appointment, Testimonial, GalleryImage
from django.test import override_settings
from datetime import datetime
import pytz


@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=False)  # Disable SSL redirect for testing
def test_home_view(client):
    # Request the home page
    response = client.get(reverse('home'))

    # Check if the status code is 200
    assert response.status_code == 200

    # Check if the correct template is used
    assert 'main/home.html' in [t.name for t in response.templates]


@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=False)  # Disable SSL redirect for testing
def test_booking_view_get(client):
    response = client.get(reverse('booking'))
    assert response.status_code == 200
    assert 'main/booking.html' in [t.name for t in response.templates]


@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=False)  # Disable SSL redirect for testing
def test_booking_view_post(client):
    data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'service': 'Haircut',
        'date': '2024-12-01T10:00:00Z',
    }
    response = client.post(reverse('booking'), data)

    expected_date = datetime(2024, 12, 1, 10, 0, tzinfo=pytz.UTC)

    # Check if the appointment was created
    assert Appointment.objects.count() == 1
    appointment = Appointment.objects.first()
    assert appointment.client_name == 'John Doe'
    assert appointment.email == 'john@example.com'
    assert appointment.service == 'Haircut'
    assert appointment.date == expected_date

    # Check if the user is redirected to the home page
    assert response.status_code == 302
    assert response.url == reverse('home')


@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=False)  # Disable SSL redirect for testing
def test_gallery_view(client):
    # Create some gallery images
    GalleryImage.objects.create(image='gallery/1.png', description='Image 1')
    GalleryImage.objects.create(image='gallery/2.png', description='Image 2')

    # Request the gallery page
    response = client.get(reverse('gallery'))

    # Check if the status code is 200
    assert response.status_code == 200

    # Check if the correct template is used
    assert 'main/gallery.html' in [t.name for t in response.templates]

    # Check if the images are in the context
    assert len(response.context['images']) == 2
    assert response.context['images'][0].description == 'Image 1'
    assert response.context['images'][1].description == 'Image 2'


@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=False)  # Disable SSL redirect for testing
def test_testimonials_view(client):
    # Create some testimonials
    Testimonial.objects.create(client_name='Jane Doe', feedback='Great service!', rating=5)
    Testimonial.objects.create(client_name='Mark Smith', feedback='Amazing haircut!', rating=4)

    # Request the testimonials page
    response = client.get(reverse('testimonials'))

    # Check if the status code is 200
    assert response.status_code == 200

    # Check if the correct template is used
    assert 'main/testimonials.html' in [t.name for t in response.templates]

    # Check if the testimonials are in the context
    assert len(response.context['testimonials']) == 2
    assert response.context['testimonials'][0].client_name == 'Jane Doe'
    assert response.context['testimonials'][1].client_name == 'Mark Smith'

    # Test that the 'range' context contains the expected range for stars (1-5)
    assert list(response.context['range']) == [1, 2, 3, 4, 5]
