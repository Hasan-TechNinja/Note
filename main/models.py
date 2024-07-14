from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

# ______________________________________unusebale table__________________________________________
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
#_____________________________________________________________________________________________________

class Notess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class SharedNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_by_user')
    shared_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_to_user')
    date = models.DateField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shared Note: {self.note.title} to {self.shared_to.username}"