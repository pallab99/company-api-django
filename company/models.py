from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)
    location = models.CharField(max_length=50, blank=False)
    about = models.TextField(blank=False)
    active = models.BooleanField(default=True, blank=False)
    type = models.CharField(max_length=50, blank=False)
    established = models.DateField(blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
