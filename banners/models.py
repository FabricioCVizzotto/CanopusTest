from django.db import models

class SavedImage(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/",storage=None, max_length=10240)


class Banner(models.Model):
    description = models.CharField(max_length=200)
    images = models.ManyToManyField(SavedImage)
