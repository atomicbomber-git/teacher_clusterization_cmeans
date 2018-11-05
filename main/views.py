from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages
import json

from .models import Dosen

@ensure_csrf_cookie
def index(request):
    dosens = serializers.serialize("json", Dosen.objects.order_by('nama') ) 
    return render(request, "main/index.html", {
        'dosens': dosens
    })

def create(request):

    Dosen.objects.create(
        nama=request.POST["nama"],
        NIP=request.POST["NIP"]
    )

    messages.success(request, 'Data berhasil ditambahkan.')

    return HttpResponseRedirect(reverse('dosen.index'))

def update(request):
    data = json.loads(request.body)

    dosen = Dosen.objects.get(id=data['id'])
    setattr(dosen, data['field'], data['value'])
    dosen.save()

    return HttpResponse(data['id'])

def delete(request, dosen_id):
    dosen = Dosen.objects.get(id=dosen_id)
    dosen.delete()
    return HttpResponse("success")

def cluster(request):
    dosens = Dosen.objects.all()
    return HttpResponse("Cluster")