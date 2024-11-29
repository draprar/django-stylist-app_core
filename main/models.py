from django.db import models


class Appointment(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
    ])

    def __str__(self):
        return f"{self.client_name} - {self.service} on {self.date}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description[:50]
