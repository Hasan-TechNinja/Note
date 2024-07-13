from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

# unusebale table--------------------------------------------------------------
class Note(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    content = HTMLField()
    create_date = models.DateField(blank=True)
    update_date = models.DateField(blank=True)
    
class Notes(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    content = HTMLField()
    create_date = models.DateField(blank=True)
    update_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
#-------------------------------------------------------------------------------

class Notess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title