from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='contacts/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
