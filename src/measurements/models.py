from django.db import models

# Create your models here.
class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Distance between {self.location}-{self.destination} is {self.distance}"
    