from django.contrib import admin
from .models import Notess

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'create_date', 'update_date')

admin.site.register(Notess, NoteAdmin)