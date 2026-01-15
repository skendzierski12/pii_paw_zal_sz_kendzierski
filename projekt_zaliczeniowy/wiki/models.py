from django.db import models


class Continent(models.Model)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    climate = models.CharField(max_length = 100)
    terrain_type = models.CharFied(max_length = 100)
