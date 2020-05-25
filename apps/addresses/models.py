from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Address(models.Model):
    """
    A simple address owned by a user.
    """
    first_name = models.CharField(max_length=128, default="")
    middle_name = models.CharField(max_length=128, default="")
    last_name = models.CharField(max_length=128, default="")

    home_no = models.CharField(max_length=64)
    mobile_no = models.CharField(max_length=64)

    address_line_1 = models.CharField(max_length=255, default="")
    address_line_2 = models.CharField(max_length=255, default="")
    address_line_3 = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=128, default="")
    postcode = models.CharField(max_length=64, default="")
    country = CountryField(null=True, default=None)

    owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="addresses")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
