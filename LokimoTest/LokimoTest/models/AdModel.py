from django.contrib.gis.db import models


class Ad(models.Model):
    ad_id = models.AutoField(primary_key=True)

    city = models.TextField(max_length=100)
    good_id = models.TextField(max_length=100)
    iris = models.TextField(max_length=100)
    data = models.JSONField()

    house = models.BooleanField()
    buy = models.BooleanField()

    last_date = models.DateField()
    first_date = models.DateField()

    meter_square = models.FloatField()
    position = models.PointField(srid=4326, null=True, blank=True)
    price = models.FloatField()
    rooms = models.FloatField()
    surface = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['ad_id']),
        ]
        ordering = ['city']
