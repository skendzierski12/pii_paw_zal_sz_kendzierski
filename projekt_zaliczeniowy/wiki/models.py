from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    climate = models.CharField(max_length = 100)
    terrain_type = models.CharField(max_length = 100)
    population = models.IntegerField()
    
    class Meta:
        verbose_name = "Kontynent"
        verbose_name_plural = "Kontynenty"
        ordering = ['population']

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=50)
    population = models.IntegerField()
    location_type = models.CharField(max_length=50)
    is_safe_from_plague = models.BooleanField(default=False)
    emblem = models.ImageField(upload_to='emblems/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Lokacja"
        verbose_name_plural = "Lokacje"
        ordering = ['name']


class Race(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    resistance = models.CharField(max_length = 50)
    homeland = models.ForeignKey(Continent, on_delete=models.CASCADE)
    traits = models.TextField()
    ethos = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Rasa"
        verbose_name_plural = "Rasy"

class Guild(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    special_traits = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Gildia"
        verbose_name_plural = "Gildie"

class Kingdom(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    capital = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    population = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Królestwo"
        verbose_name_plural = "Królestwa"
        ordering = ['population']


class Plague(models.Model):
    description = models.TextField(help_text="Opis plagi")
    history = models.TextField(help_text="Historia - jak to wszystko się zaczęło")
    symptomps = models.TextField(help_text="Objawy")
    death = models.IntegerField(help_text="Szacunkowa liczba osób które umarły przez zarażenie")
    epicentre = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Plaga"
        verbose_name_plural = "Informacje o pladze"
    
    def __str__(self):
        return "Informacje o pladze"
    
    def save(self, *args, **kwargs):
        if not self.pk and Plague.objects.exists():
            raise ValueError("Może istnieć tylko jeden rekord")
        return super().save(*args, **kwargs)

class Epicentre(Location):
    DANGER_LEVELS = [
            ('low', 'Niski'),
            ('medium', 'Umiarkowany'),
            ('high', 'Wysoki'),
            ('deathly', 'Śmiertelny'),
            ]
    infection_rate = models.IntegerField(help_text="Procent zarażonych (0-100)")
    deaths_here = models.IntegerField(help_text="Ilość zgonów")
    danger_level = models.CharField(max_length=20, choices=DANGER_LEVELS, default='medium')
    
    class Meta:
        verbose_name = "Epicentrum plagi"
        verbose_name_plural = "Epicentra plagi"

    def __str__(self):
        return f"Epicentrum: {self.name} ({self.get_danger_level_display()})"



class Item(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    effect = models.CharField(max_length = 100, null = True, blank = True)
    def __str__(self):
        return self.name


