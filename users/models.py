from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """Costum User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_PERSIAN = "fa"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_PERSIAN, "Persian"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_IRRIAL = "irrials"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_IRRIAL, "IRRIALS"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=7, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
