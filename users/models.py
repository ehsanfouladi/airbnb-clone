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

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
    )
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=7,
        blank=True,
    )
    superhost = models.BooleanField(default=False)
