from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    bluetooth_exists = models.BooleanField()
    os = models.CharField(max_length=15)
    megapixels = models.IntegerField()
    ram = models.IntegerField()
    rom = models.IntegerField()
    screen = models.CharField(max_length=40)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
