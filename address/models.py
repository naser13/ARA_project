from django.db import models


class Address(models.Model):
    pass


class Province(models.Model):
    name = models.CharField(max_length=100, default='تهران')


class City(models.Model):
    name = models.CharField(max_length=100, default='تهران')
    province = models.ForeignKey(Province, default=1)