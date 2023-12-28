from django.db import models
from base.models import BaseModel
from django.core.validators import MinLengthValidator


# Create your models here.


class Company(BaseModel):
    name = models.CharField(max_length=50, unique=True, blank=False, validators=[
                            MinLengthValidator(5, "Name must be at least 5 characters")])
    location = models.CharField(max_length=50, blank=False, validators=[
        MinLengthValidator(5, "Location must be at least 5 characters")])
    about = models.TextField(blank=False, validators=[
        MinLengthValidator(10, "About must be at least 10 characters")])
    active = models.BooleanField(default=True, blank=False)
    type = models.CharField(max_length=50, blank=False)
    established = models.DateField(blank=False)

    def __str__(self) -> str:
        return str(self.name)
