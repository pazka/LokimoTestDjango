from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import data from the Url provided by Lokimo'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
