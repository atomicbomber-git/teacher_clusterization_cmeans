from django.shortcuts import render
from django.http import HttpResponse
from .models import Dosen

def index(request):
    dosens = Dosen.objects.all()
    return render(request, "main/index.html", {
        'dosens': Dosen.objects.all()
    })
