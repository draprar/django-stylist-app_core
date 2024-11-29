import pytest
from main.models import Appointment, Testimonial, GalleryImage


@pytest.mark.django_db
def test_appointment_model():
    # Create an Appointment
    appointment = Appointment.objects.create(
        client_name='John Doe',
        email='john@example.com',
        service='Haircut',
        date='2024-12-01T10:00:00Z',
        status='Pending'
    )

    # Test the string representation
    assert str(appointment) == 'John Doe - Haircut on 2024-12-01T10:00:00Z'


@pytest.mark.django_db
def test_testimonial_model():
    # Create a Testimonial
    testimonial = Testimonial.objects.create(
        client_name='Jane Doe',
        feedback='Great service!',
        rating=5
    )

    # Test the string representation
    assert str(testimonial) == 'Jane Doe - 5 stars'


@pytest.mark.django_db
def test_gallery_image_model():
    # Create a GalleryImage
    gallery_image = GalleryImage.objects.create(
        image='gallery/1.png',
        description='Beautiful haircut'
    )

    # Test the string representation
    assert str(gallery_image) == 'Beautiful haircut'  # it returns the first 50 characters of the description
