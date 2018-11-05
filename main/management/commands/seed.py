from django.core.management.base import BaseCommand, CommandError
from main.models import Dosen

import random
import factory
import factory.django

class DosenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dosen
    
    nama = factory.Faker("name")
    NIP = factory.Faker("phone_number")
    nilai_1 = random.randint(0, 10000) / 100
    nilai_2 = random.randint(0, 10000) / 100
    nilai_3 = random.randint(0, 10000) / 100
    nilai_4 = random.randint(0, 10000) / 100
    nilai_5 = random.randint(0, 10000) / 100
    nilai_6 = random.randint(0, 10000) / 100
    nilai_7 = random.randint(0, 10000) / 100
    nilai_8 = random.randint(0, 10000) / 100
    nilai_9 = random.randint(0, 10000) / 100
    nilai_10 = random.randint(0, 10000) / 100
    nilai_11 = random.randint(0, 10000) / 100
    nilai_12 = random.randint(0, 10000) / 100
    nilai_13 = random.randint(0, 10000) / 100
    nilai_14 = random.randint(0, 10000) / 100
    nilai_15 = random.randint(0, 10000) / 100
    nilai_16 = random.randint(0, 10000) / 100
    nilai_17 = random.randint(0, 10000) / 100
    cluster = 0

class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        print('Seeding Dosen...')

        for _ in range(200):
            DosenFactory.create()
