from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField
# Create your models here.

class PostYoz(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=160,blank=True)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True)
    image = models.CharField(max_length=400,default="https://media-exp1.licdn.com/dms/image/C561BAQGQ6dIcBhfqaw/company-background_10000/0/1526873579149?e=2159024400&v=beta&t=_2aB5pycriIFXMGz_KbKNumpcy28CgpnzC5cq-Iw81w")
    
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=40)
    video = EmbedVideoField() 
    
    def __str__(self):
        return self.title



