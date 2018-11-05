from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dosen.index'),
    path('/update', views.update, name='dosen.update')
]