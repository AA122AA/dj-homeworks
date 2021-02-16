from django.db import models

class Ram(models.TextChoices):
        gb16 = "16GB"
        gb8 = "8GB"
        gb4 = "4GB"
        other = "Other"
        kb1 = "1KB"

class Rom(models.TextChoices):
        gb64 = "64GB"
        gb128 = "128GB"
        gb256 = "256GB"
        other = "Other"
        kb1 = "1KB"

class OS(models.TextChoices):
        adroid = "Android"
        ios = "IOS"
        other = "Other"

class Phone(models.Model):
    name = models.CharField(max_length=50, default="phone")
    price = models.IntegerField(default=10)
    release_date = models.DateField(default="2000-09-01")
    lte_exists = models.BooleanField(default=True)
    bluetooth_exists = models.BooleanField(default=True)
    os = models.CharField(choices= OS.choices, max_length=15, blank=True)
    camera_amount = models.IntegerField(default=1)
    ram = models.TextField(choices = Ram.choices, blank=True)
    rom = models.TextField(choices = Rom.choices, blank=True)
    screen = models.CharField(max_length=40, blank=True)
    battery = models.IntegerField(default=3000)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
class Samsung(Phone):
    Dex = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Apple(Phone):
    FaceId = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Nokia(Phone):
    Durability = models.TextField(max_length=15, default="Great")

    def __str__(self):
        return self.name