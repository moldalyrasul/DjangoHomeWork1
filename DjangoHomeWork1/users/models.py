from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )
    OCUP_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
        ("MILLIONAIRE", "MILLIONAIRE")
    )
    password1 = models.CharField(max_length=100, null=True)
    password2 = models.CharField(max_length=100, null=True)
    patronymic = models.CharField(max_length=100, null=True)
    phone_number = models.CharField("phone-number", max_length=60, unique=True)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Гендер")
    date_of_birth = models.DateField(null=True)
    growth = models.IntegerField(null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    occupation = models.CharField(choices=OCUP_CHOICE, max_length=80)