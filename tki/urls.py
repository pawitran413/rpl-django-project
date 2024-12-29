from django.urls import path
from . import views

urlpatterns = [
    path('tki/', views.tki, name='tki'),
    path('tki/details/<int:id>', views.details, name='details'),
    path('tki/details/<int:id>/matkul', views.matkul, name='matkul')
]