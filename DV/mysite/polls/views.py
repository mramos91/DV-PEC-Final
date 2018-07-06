



# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import pandas as pd	



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
	
def home(request):
    return render(request, 'home.html')


@csrf_exempt
def prueba(request):
	
	result_set = {"response":[],"error":"" }
	
	lista  =[]
	with open('datos.csv', 'r') as archivo_lectura:
		b  = {}
		b['key'] = "TITULO"
		b['values']=[]
		for linea in archivo_lectura:
			a = {}
			a['label'] = linea.split(',')[0]
			a['value'] = round(float(linea.split(',')[1].strip()),2)
			b['values'].append(a)
		lista.append(b)
	result_set["response"] = lista		
	
	return JsonResponse(result_set, safe=False)
	
	

@csrf_exempt
def prueba2(request):
	
	result_set = {"response":[],"error":"" }
	
	lista  =[]
	with open('datos2.csv', 'r') as archivo_lectura:
		b  = {}
		b['key'] = "TITULO"
		b['values']=[]
		for linea in archivo_lectura:
			a = {}
			a['label'] = linea.split(',')[0]
			a['value'] = round(float(linea.split(',')[1].strip()),2)
			b['values'].append(a)
		lista.append(b)
	result_set["response"] = lista		
	
	return JsonResponse(result_set, safe=False)