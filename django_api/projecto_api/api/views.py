from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json

# Create your views here.


class CompanyView(View):
    
    #este metodo ayuda a que evita el error del csrf
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if id > 0:
            #http://127.0.0.1:8000/api/companies/2
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': 'success', 'company': company}
            else:
                datos = {'message': 'company not fount...'}
            return JsonResponse(datos)
        else: 
            # se debe devolver una lista
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message': 'Success', 'companies':companies}
            else:
                datos = {'message': 'Companies not found'}
            return JsonResponse(datos)

    def post(self, request):
        #un registro
        #print(request.body)
        datos_json = json.loads(request.body)
        print(datos_json)
        
        Company.objects.create(name=datos_json['name'], wedsite=datos_json['website'], fundation=datos_json['fundation'])
        datos = {'mensaje': 'Success'}
        return JsonResponse(datos)
    
    
    def put(self, request, id):
        jd = json.loads(request.body)
        company = list(Company.objects.filter(id=id).values_list())
        if len(company) > 0:
            c = Company.objects.get(id=id)
            c.name = jd['name']
            c.website = jd['website']
            c.fundation = jd['fundation']
            c.save()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Company not fount'}
            
        return JsonResponse(datos)  
            


