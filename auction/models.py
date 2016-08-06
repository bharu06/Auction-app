from __future__ import unicode_literals

from django.db import models

# Create your models here.

# item anedi singlular aa plural aa ? Per emi undali ?arey table kada anduke items ani kept ,oho ala vachava ,ento emo
class items(models.Model):
    Description=models.CharField(max_length=40)
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='pictures')
    username=models.CharField(max_length=40)
    price=models.IntegerField()
    def __unicode__(self):
        return self.name

class bids(models.Model):
    username=models.CharField(max_length=40)
    item_id=models.ForeignKey(items)
    price=models.IntegerField()
    def __unicode__(self):
        return self.username

