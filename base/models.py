from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    ROLES = (
        ('TE', 'معلم'),
        ('HM', 'مدیر'),
        ('ST', 'دانش آموز'),
    )

    role = models.CharField(max_length=2, choices=ROLES)


class Teacher(Person):
    pass


class HeadMaster(Person):
    pass


class Student(Person):
    pass