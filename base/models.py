from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    pass


class Teacher(models.Model):
    user = models.ForeignKey(Person, unique=True)


class HeadMaster(models.Model):
    user = models.ForeignKey(Person, unique=True)


class Student(models.Model):
    user = models.ForeignKey(Person, unique=True)