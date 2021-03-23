from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Offer(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill)
    date_added = models.CharField(max_length=200)
    exp = models.CharField(max_length=200)

    def __str__(self):
        return self.name
