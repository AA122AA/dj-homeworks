from django.db import models

class Ram(models.IntegerChoices):
        gb16 = 16, "16gb"
        gb8 = 8, "8gb"
        gb4 = 4, "4gb"
        other = 0, "Other"

class Rom(models.IntegerChoices):
        gb64 = 64, "64gb"
        gb128 = 128, "128gb"
        gb256 = 256, "256gb"
        other = 0, "Other"

class OS(models.TextChoices):
        adroid = "Android"
        ios = "IOS"
        other = "Other"

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    bluetooth_exists = models.BooleanField()
    os = models.CharField(choices= OS.choices, max_length=15)
    megapixels = models.IntegerField()
    ram = models.IntegerField(choices = Ram.choices)
    rom = models.IntegerField(choices = Rom.choices)
    screen = models.CharField(max_length=40)
    slug = models.SlugField()
    battery = models.IntegerField()

    def __str__(self):
        return self.name
    
class Samsung(Phone):
    Dex = models.BooleanField()

class Apple(Phone):
    FaceId = models.BooleanField()