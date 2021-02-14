import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from slugify import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')
            # пропускаем заголовок
            #next(phone_reader)
            for line in phone_reader:
                line["slug"] = slugify(line.get("name"))
                if Phone.objects.filter(id=line["id"]).exists():
                    p = Phone.objects.filter(id=line.get("id")).update(**line)
                else:
                    p = Phone.objects.create(**line)

