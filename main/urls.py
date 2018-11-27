from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dosen.index'),
    path('update', views.update, name='dosen.update'),
    path('create', views.create, name='dosen.create'),
    path('view', views.view, name='dosen.view'),
    path('delete/<int:dosen_id>', views.delete, name='dosen.delete'),
    path('cluster', views.cluster, name='dosen.cluster')
]