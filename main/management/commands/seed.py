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
    nilai_1 =  lambda x: random.randint(0, 10000) / 100
    nilai_2 =  lambda x: random.randint(0, 10000) / 100
    nilai_3 =  lambda x: random.randint(0, 10000) / 100
    nilai_4 =  lambda x: random.randint(0, 10000) / 100
    nilai_5 =  lambda x: random.randint(0, 10000) / 100
    nilai_6 =  lambda x: random.randint(0, 10000) / 100
    nilai_7 =  lambda x: random.randint(0, 10000) / 100
    nilai_8 =  lambda x: random.randint(0, 10000) / 100
    nilai_9 =  lambda x: random.randint(0, 10000) / 100
    nilai_10 = lambda x: random.randint(0, 10000) / 100
    nilai_11 = lambda x: random.randint(0, 10000) / 100
    nilai_12 = lambda x: random.randint(0, 10000) / 100
    nilai_13 = lambda x: random.randint(0, 10000) / 100
    nilai_14 = lambda x: random.randint(0, 10000) / 100
    nilai_15 = lambda x: random.randint(0, 10000) / 100
    nilai_16 = lambda x: random.randint(0, 10000) / 100
    nilai_17 = lambda x: random.randint(0, 10000) / 100
    cluster = 0

class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        print('Seeding Dosen...')

        for _ in range(50):
            DosenFactory.create()
