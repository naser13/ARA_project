from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    pass


class Teacher(Person):
    pass


class HeadMaster(Person):
    pass


class Student(Person):
    pass