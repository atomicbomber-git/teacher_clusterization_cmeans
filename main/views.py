from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages
import json
from .models import Dosen
from . import cmeans


@ensure_csrf_cookie
def index(request):
    dosens = serializers.serialize("json", Dosen.objects.order_by('nama'))
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
    n_cluster = int(request.POST.get("cluster", 2))
    dosens = [dosen.as_dict() for dosen in Dosen.objects.all()]

    processed_data = {}

    for record in dosens:
        record_id = record['id']
        del record['id']
        del record['nama']
        del record['NIP']
        processed_data[record_id] = record

    features = [
        'nilai_1', 'nilai_2', 'nilai_3', 'nilai_4', 'nilai_5', 'nilai_6', 'nilai_7', 'nilai_8',
        'nilai_9', 'nilai_10', 'nilai_11', 'nilai_12', 'nilai_13', 'nilai_14', 'nilai_15', 'nilai_16',
        'nilai_17',
    ]

    clusters = cmeans.clusterize(processed_data, features=features, n_cluster=n_cluster, n_iteration=200)
    
    for dosen_id, cluster in clusters.items():
        dosen = Dosen.objects.get(id=dosen_id)
        dosen.cluster = cluster
        dosen.save()
    
    return HttpResponseRedirect(reverse('dosen.index'))
