from django.db import models



class Tarief(models.Model):
    starttarief = models.FloatField()
    per_kilometer = models.FloatField()