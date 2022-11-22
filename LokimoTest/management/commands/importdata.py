import json

import requests
from django.core.management.base import BaseCommand
from rest_framework.exceptions import ValidationError

from LokimoTest.LokimoTest.domain.ad_serializer import AdFullDTOSerializer
from LokimoTest.LokimoTest.services.error_wrapper import ServerError


class Command(BaseCommand):
    help = 'Import data from the Url provided by Lokimo'

    def handle(self, *args, **options):
        r = requests.get('https://lokimo-map.s3.eu-west-3.amazonaws.com/lokimo-dataset-backend-test.json')
        self.stdout.write(self.style.SUCCESS('Successfully downloaded data'))
        data = r.json()
        nb_item = len(data)
        nb_imported_item = 0
        self.stdout.write(self.style.SUCCESS(f'Detected {nb_item} items'))
        for item in data:
            serializer = AdFullDTOSerializer(data=item)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except ValidationError as e:
                self.stdout.write(self.style.FAIERROR(f'Import failed at item#{nb_imported_item+1}'))
                raise ServerError(e.detail)
            nb_imported_item += 1

        self.stdout.write(self.style.SUCCESS('Successfully imported all data'))
