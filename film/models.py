from django.db import models #type: ignore

class Film(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    directed = models.CharField(max_length=255)
    year = models.IntegerField()
    image = models.ImageField(upload_to='film/media/images', blank=True, null=True)

    def __str__(self):
        return self.name
