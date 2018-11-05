from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Dosen

def index(request):
    dosens = Dosen.objects.all()
    return render(request, "main/index.html", {
        'dosens': Dosen.objects.all()
    })

def update(request):
    return JsonResponse(request.POST.get("data"), safe=False)


    return HttpResponseRedirect(reverse('dosen.index'))