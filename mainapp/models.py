from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200)


class Offer(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill)