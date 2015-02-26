from django.shortcuts import render
from .settings import google_key

# Create your views here.

def home(request):
    return render(request, 'app/index.html', {'google_key': google_key})