from django.db import models

class UrlShortner(models.Model):
    url = models.TextField()
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return self.uuid

