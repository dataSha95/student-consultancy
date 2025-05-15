from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
