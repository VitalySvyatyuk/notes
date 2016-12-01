from django.shortcuts import render
# from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
                                                                  
from .models import Note
 
  
def index(request):
    return render(request, 'index.html', {})
  
@login_required
def mynotes(request):
    notes = Note.objects.all()
    return render(request, 'mynotes.html', { 'notes': notes })