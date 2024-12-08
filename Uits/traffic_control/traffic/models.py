# traffic/models.py

from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()  # Date of Birth
    nid = models.CharField(max_length=20)  # National ID
    present_address = models.TextField()
    permanent_address = models.TextField()
    image = models.ImageField(upload_to='owner_images/')
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    licence_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

LicenceOwner = Owner

class Fine(models.Model):
    licence_number = models.ForeignKey(LicenceOwner, on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=255)
    violation_time = models.DateTimeField()
    violation_location = models.CharField(max_length=255)

class Expiry(models.Model):
    licence_number = models.ForeignKey(LicenceOwner, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"