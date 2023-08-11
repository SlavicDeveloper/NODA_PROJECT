from django.shortcuts import render
from django.views import generic
from .models import Notes


def NotesPreview(request):
    docs = Notes.objects.all()
    return render(request, "main/notes_preview.html", context={'notes': docs})


def index(request):
    return render(request, 'main/index.html')
