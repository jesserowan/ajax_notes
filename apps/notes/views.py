from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt

def index(request):
    notes = Note.objects.all().order_by('-created_at')
    context = {
        "notes" : notes
    }
    return render(request, 'notes/index.html', context)


def add(request):
    if request.method == 'POST':
        errors = Note.objects.validate(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        else:
            Note.objects.create(title=request.POST['title'], description=request.POST['description'])
        
    context = {
        "notes": Note.objects.all().order_by('-created_at')
    }
    return render(request, 'notes/notes_index.html', context)
    
@csrf_exempt
def delete(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.delete()
    context = {
        "notes": Note.objects.all().order_by('-created_at')
    }
    return render(request, 'notes/notes_index.html', context)

def edit(request, id):
    if request.method == "POST":
        note = Note.objects.get(id=id)
        note.description = request.POST['edit_description']
        note.save()
    context = {
        "notes": Note.objects.all().order_by('-created_at')
    }
    return render(request, 'notes/notes_index.html', context)
