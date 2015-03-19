from django.db import models


class Address(models.Model):
    pass


class Province(models.Model):
    name = models.CharField(max_length=100, default='تهران')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, default='تهران')
    province = models.ForeignKey(Province, default=1)

    def __str__(self):
        return self.name