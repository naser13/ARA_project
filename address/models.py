from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province)

    def __str__(self):
        return self.name


class Address(models.Model):
    province = models.ForeignKey(Province, default=1)
    city = models.ForeignKey(City, default=1)
    street = models.CharField(max_length=100, default='')
