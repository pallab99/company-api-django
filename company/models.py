from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel


class Company(BaseModel):
    """
    Represents a company entity with various fields to store information about the company.
    """

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        unique=True,
        blank=False,
        validators=[MinLengthValidator(
            5, _("Name must be at least 5 characters")), MaxLengthValidator(100, _("Name can not be greater than 100 characters"))]
    )
    location = models.CharField(
        verbose_name=_("Location"),
        max_length=100,
        blank=False,
        validators=[MinLengthValidator(
            5, _("Location must be at least 5 characters")), MaxLengthValidator(100, _("Location can not be greater than 100 characters"))]
    )
    about = models.TextField(
        verbose_name=_("About"),
        blank=False,
        validators=[MinLengthValidator(
            10, _("About must be at least 10 characters"))]
    )
    active = models.BooleanField(
        verbose_name=_("Active"),
        blank=False,
        default=True
    )
    company_type = models.CharField(
        verbose_name=_("Type"),
        max_length=100,
        blank=False,
        help_text=_("Type of the company"),
        default="IT",
        validators=[MinLengthValidator(
            1, _("Company Type must be at least 1 characters")), MaxLengthValidator(100, _("Company Type can not be greater than 100 characters"))]
    )
    established = models.DateField(
        verbose_name=_("Established"),
        blank=False,
        help_text=_("Date when the company was established")
    )

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        """
        Returns a string representation of the company object, which is its name.
        """
        return self.name
