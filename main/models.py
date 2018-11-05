from django.db import models

class Dosen(models.Model):
    nama = models.CharField(max_length=50)
    NIP = models.CharField(max_length=50,unique=True)
    nilai_1 = models.FloatField(default=0)
    nilai_2 = models.FloatField(default=0)
    nilai_3 = models.FloatField(default=0)
    nilai_4 = models.FloatField(default=0)
    nilai_5 = models.FloatField(default=0)
    nilai_6 = models.FloatField(default=0)
    nilai_7 = models.FloatField(default=0)
    nilai_8 = models.FloatField(default=0)
    nilai_9 = models.FloatField(default=0)
    nilai_10 = models.FloatField(default=0)
    nilai_11 = models.FloatField(default=0)
    nilai_12 = models.FloatField(default=0)
    nilai_13 = models.FloatField(default=0)
    nilai_14 = models.FloatField(default=0)
    nilai_15 = models.FloatField(default=0)
    nilai_16 = models.FloatField(default=0)
    nilai_17 = models.FloatField(default=0)
    cluster = models.IntegerField(default=0)

    def as_dict(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'NIP': self.NIP,
            'nilai_1': self.nilai_1,
            'nilai_2': self.nilai_2,
            'nilai_3': self.nilai_3,
            'nilai_4': self.nilai_4,
            'nilai_5': self.nilai_5,
            'nilai_6': self.nilai_6,
            'nilai_7': self.nilai_7,
            'nilai_8': self.nilai_8,
            'nilai_9': self.nilai_9,
            'nilai_10': self.nilai_10,
            'nilai_11': self.nilai_11,
            'nilai_12': self.nilai_12,
            'nilai_13': self.nilai_13,
            'nilai_14': self.nilai_14,
            'nilai_15': self.nilai_15,
            'nilai_16': self.nilai_16,
            'nilai_17': self.nilai_17,
        }