from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='universities/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
