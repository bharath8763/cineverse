from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    duration = models.CharField(max_length=50)
    description = models.TextField()

    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)  # 👈 NEW

    def __str__(self):
        return self.title
