from django.db import models
from django.utils.html import format_html


# Create your models here.
class container(models.Model):
    container_id = models.AutoField(primary_key=True)
    container_title = models.CharField(max_length=100)
    container_des = models.TextField()
    container_url = models.CharField(max_length=100)
    container_image = models.ImageField(upload_to='container/')

    def content(self):
        return format_html('<img src: "media/{}"  />'.format(self.container_image))

class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_des = models.TextField()
    post_url = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='posts/')
