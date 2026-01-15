from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    climate = models.CharField(max_length = 100)
    terrain_type = models.CharFied(max_length = 100)

class Location(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    population = models.IntegerField()
    is_safe_from_plague = models.BooleanField(default=False)
    emblem = models.ImageField()

class Race(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    resistance = models.TextChoices()
    homeland = models.ForeignKey(Continent, on_delete=models.CASCADE)
    traits = models.TextField()
    ethos = models.CharField(max_lenght = 1500)

class Guild(models.Model):
    name = models.CharField(max_lenght = 100)
    description = models.TextField()
    special_traits = models.TextField()

class Kingdom(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    population = models.IntegerField()
    homeland = models.ForeignKey(Continent, on_delete=models.CASCADE)

class Plague(models.Model):
    description = models.TextField()
    history = models.TextField()
    symptomps = models.TextField()
    death = models.IntegerField()
    epicentre = models.ForeignKey(Location, on_delete=models.CASCADE)


class Item(models.Model):
    type = models.ForeignKey(Item_type, on_delete=models.CASCADE)
    name = models.CharField(max_lenght = 100)
    description = models.TextField()


