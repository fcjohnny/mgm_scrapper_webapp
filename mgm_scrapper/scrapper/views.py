from django.shortcuts import render
from django.http import HttpResponse
from .mgm_scrapper import scrap
import datetime

# Create your views here.
def index(request):
  json_data = scrap('json_data')
  response = HttpResponse(json_data, content_type='application/json')
  response['Content-Disposition'] = 'attachment;\
  filename="'+datetime.datetime.now().strftime('%Y-%m-%d')+'.xls"'
  return response
