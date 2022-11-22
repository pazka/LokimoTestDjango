from rest_framework import serializers

from LokimoTest.LokimoTest.models.AdModel import Ad


class AdFullDTOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ad
        exclude = []  # fetch all the fields
