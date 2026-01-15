from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    climate = models.CharField(max_length = 100)
    terrain_type = models.CharField(max_length = 100)
def __str__(self):
    return self.name

class Location(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    population = models.IntegerField()
    location_type = models.CharField(max_length=50)
    is_safe_from_plague = models.BooleanField(default=False)
    emblem = models.ImageField(upload_to='emblems/', blank=True, null=True)
    
def __str__(self):
    return self.name

class Race(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    resistance = models.TextField() #TextChoices()
    homeland = models.ForeignKey(Continent, on_delete=models.CASCADE)
    traits = models.TextField()
    ethos = models.TextField()
def __str__(self):
    return self.name

class Guild(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    special_traits = models.TextField()
def __str__(self):
    return self.name

class Kingdom(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    population = models.IntegerField()
    homeland = models.ForeignKey(Continent, on_delete=models.CASCADE)
def __str__(self):
    return self.name

class Plague(models.Model):
    description = models.TextField()
    history = models.TextField()
    symptomps = models.TextField()
    death = models.IntegerField()
    epicentre = models.ForeignKey(Location, on_delete=models.CASCADE)
def __str__(self):
    return self.name


class Item(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
def __str__(self):
    return self.name


