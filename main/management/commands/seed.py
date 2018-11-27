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
    nilai_1 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_2 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_3 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_4 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_5 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_6 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_7 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_8 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_9 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100)  
    nilai_10 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    nilai_11 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    nilai_12 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    nilai_13 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    nilai_14 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    nilai_15 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    nilai_16 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    nilai_17 = factory.LazyAttribute(lambda x: random.randint(0, 10000) / 100) 
    kelas = 'A'
    kode_mk = 'AX123' 
    mata_kuliah = 'Bahasa Perancis' 
    cluster = 0

class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **options):
        print('Seeding Dosen...')

        for _ in range(50):
            DosenFactory.create()
