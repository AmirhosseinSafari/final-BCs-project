#from datetime import datetime
#from django.utils import timezone
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    url = models.URLField()
    image = models.URLField(blank=True, null=True)
    short_description = models.URLField(blank=True, null=True)
    news_time = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return  f"{self.title}: {self.short_description}  link ==> {self.url}, time: {self.news_time}"