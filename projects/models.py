from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
fs = FileSystemStorage(location='/media/photos')

class Project(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    # image = models.FilePathField(path = "/img")
    image =  models.ImageField(upload_to=fs, blank=True, null=True)