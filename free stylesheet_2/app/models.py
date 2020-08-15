from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    def __str__(self):
        return self.name