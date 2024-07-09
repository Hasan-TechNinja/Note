from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Notes
from datetime import date
from .forms import NoteForm

def home(request):
    notes = Notes.objects.all()
    context = {
        "notes": notes
    }
    return render(request, 'home.html', context)

def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.create_date = date.today()
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'create.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    note.delete()
    return redirect('home')

def show_note(request, note_id):
    show = get_object_or_404(Notes, id=note_id)
    context = {
        "show":show
    }
    return render(request, 'show_note.html', context)

def update_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form,
        'note': note
    }
    return render(request, 'update_note.html', context)