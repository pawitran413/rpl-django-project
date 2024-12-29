from django.http import HttpResponse
from django.template import loader
from .models import Tki

def tki(request):
  sometki = Tki.objects.all().values()
  template = loader.get_template('mhstki.html')
  context = {
    'sometki': sometki,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  sometki = Tki.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'sometki': sometki,
  }
  return HttpResponse(template.render(context, request))

def matkul(request, id):
  idmhs = Tki.objects.get(id=id)
  template = loader.get_template('matkul.html')
  context = {
    'idmhs': idmhs,
  }
  return HttpResponse(template.render(context, request))