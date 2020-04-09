from django.db import models
import os,re
from django.conf import settings
def upload_img(instance, filename):
    if os.path.isdir(settings.BASE_DIR+'/Media/img'): # will go in if statement, if required directory is exist.
        print("img dir exists")
        return os.path.join('img/'+"%s" %(re.sub('[^a-zA-Z0-9 \.\_]', '', filename).replace(' ', ''), ))
    else:
        os.makedirs(settings.BASE_DIR+'/Media/img')
        print("img dir not exists creating one")
        return os.path.join('img/'+"%s" %(re.sub('[^a-zA-Z0-9 \.\_]', '', filename).replace(' ', ''), ))
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    image = models.FileField(upload_to = upload_img)

