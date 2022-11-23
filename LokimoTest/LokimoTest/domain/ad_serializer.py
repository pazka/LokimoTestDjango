from django.contrib.gis.geos import Point
from rest_framework import serializers

from LokimoTest.LokimoTest.models.AdModel import Ad


class AdFullDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = []  # fetch all the fields

    def create(self, validated_data):
        position_geo = None
        position_json = validated_data.pop('position')
        if position_json is not None:
            position_geo = Point(x=position_json['lat'], y=position_json['lng'])

        return Ad.objects.create(position=position_geo, **validated_data)
