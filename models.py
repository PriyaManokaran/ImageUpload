from django.db import models

# Create your models here.

class File(models.Model):
    file = models.ImageField(upload_to='media',max_length=255)
    def __str__(self):
        return self.file.name