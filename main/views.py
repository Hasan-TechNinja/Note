from django.shortcuts import render, redirect, get_object_or_404
from .models import Notess
from datetime import date
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

@login_required
def home(request):
    notes = Notess.objects.filter(user=request.user)
    context = {
        "notes": notes
    }
    return render(request, 'home.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.create_date = date.today()
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'create.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Notess, id=note_id, user=request.user)
    note.delete()
    return redirect('home')

@login_required
def show_note(request, note_id):
    show = get_object_or_404(Notess, id=note_id, user=request.user)
    context = {
        "show": show
    }
    return render(request, 'show_note.html', context)

@login_required
def update_note(request, note_id):
    note = get_object_or_404(Notess, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note.create_date = date.today()
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form,
        'note': note
    }
    return render(request, 'update_note.html', context)

def Registration(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm = UserCreationForm()
    context = {
        "form": fm,
    }
    return render(request, 'registration.html', context)

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', 'home')
                return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form, 'next': request.GET.get('next', '')})

def Logout(request):
    logout(request)
    return redirect('login')
