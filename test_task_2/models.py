from django.contrib.gis.db import models
from django.db.models import ForeignKey


class Map(models.Model):
    name = models.CharField(max_length=40)


class TestFields(models.Model):
    mpoly = models.MultiPolygonField(srid=4269)
    productivi = models.IntegerField()
    field = ForeignKey(Map, on_delete=models.CASCADE, default=1)
