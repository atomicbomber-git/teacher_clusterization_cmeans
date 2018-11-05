#!python

from django_seed import Seed
import random

seeder = Seed.seeder

from main.models import Dosen
seeder.add_entity(Dosen, 100, {
    'score_1': lambda x: random.randint(0, 10000) / 100,
    'score_2': lambda x: random.randint(0, 10000) / 100,
    'score_3': lambda x: random.randint(0, 10000) / 100,
    'score_4': lambda x: random.randint(0, 10000) / 100,
    'score_5': lambda x: random.randint(0, 10000) / 100,
    'score_6': lambda x: random.randint(0, 10000) / 100,
    'score_7': lambda x: random.randint(0, 10000) / 100,
    'score_8': lambda x: random.randint(0, 10000) / 100,
    'score_9': lambda x: random.randint(0, 10000) / 100,
    'score_10': lambda x: random.randint(0, 10000) / 100,
    'score_11': lambda x: random.randint(0, 10000) / 100,
    'score_12': lambda x: random.randint(0, 10000) / 100,
    'score_13': lambda x: random.randint(0, 10000) / 100,
    'score_14': lambda x: random.randint(0, 10000) / 100,
    'score_15': lambda x: random.randint(0, 10000) / 100,
    'score_16': lambda x: random.randint(0, 10000) / 100,
    'score_17': lambda x: random.randint(0, 10000) / 100,
})

seeder.execute()