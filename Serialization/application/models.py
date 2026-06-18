from django.db import models

class MovieModels(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=30)
    hero = models.CharField(max_length=50)
    heroine = models.CharField(max_length=50)
    director = models.CharField(max_length=40)
    music = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} is directed by {self.director}"
    