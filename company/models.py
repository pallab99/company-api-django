from django.db import models
from base.models import BaseModel
# Create your models here.


class Company(BaseModel):
    name = models.CharField(max_length=50, unique=True, blank=False)
    location = models.CharField(max_length=50, blank=False)
    about = models.TextField(blank=False)
    active = models.BooleanField(default=True, blank=False)
    type = models.CharField(max_length=50, blank=False)
    established = models.DateField(blank=False)

    def __str__(self) -> str:
        return str(self.name)
