from django.shortcuts import render, redirect

# Create your views here.


# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse

from general.forms import *
from .models import * 


def menu_principal(request):
	return render(request, 'menu_principal.html', {})


def nueva_ficha(request):
	form1 = FichaCensoForm()

	if request.POST:
		ficha = FichaCenso()
		# departamentos = Departamentos()
		# municipios = Municipios()		

		ficha.primer_apellido = None if request.POST.get('primer_apellido') == '' else request.POST.get('primer_apellido')
		ficha.segundo_apellido = None if request.POST.get('segundo_apellido') == '' else request.POST.get('segundo_apellido')
		ficha.identidad = None if request.POST.get('identidad') == '' else request.POST.get('identidad')
		ficha.nombres = None if request.POST.get('nombres') == '' else request.POST.get('nombres')
		ficha.fecha_nacimiento = None if request.POST.get('fecha_nacimiento ') == '' else request.POST.get('fecha_nacimiento')
		ficha.cod_departament_nacimiento = Departamentos.objects.get(pk=request.POST.get('cod_departament_nacimiento'))
		ficha.cod_municipio_nacimiento = Municipios.objects.get(pk=request.POST.get('cod_municipio'))
		ficha.edad = None if request.POST.get('edad') == '' else request.POST.get('edad')
		ficha.numero_afiliado = None if request.POST.get('numero_afiliado') == '' else request.POST.get('numero_afiliado')
		ficha.genero = None if request.POST.get('genero') == '' else request.POST.get('genero')
		ficha.estado_civil = None if request.POST.get('estado_civil') == '' else request.POST.get('estado_civil')
		ficha.cod_estado = Estados.objects.get(pk=0)
		ficha.save()
		return redirect(reverse('nueva_ficha_2', kwargs={'cod_censo': ficha.cod_censo}))

	return render(request, 'nueva_ficha.html', {'form1': form1})


def nueva_ficha_2(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)

			ficha = FichaCenso()
			ficha.nivel_educativo = None if request.POST.get('nivel_educativo') == '' else request.POST.get('nivel_educativo')
			ficha.cod_profesion_oficio = ProfesionOficio.objects.get(pk=request.POST.get('cod_profesion_oficio'))
			ficha.cod_departament_domicilio = Departamentos.objects.get(pk=request.POST.get('cod_departamenton'))
			ficha.cod_municipio_domicilio = Municipios.objects.get(pk=request.POST.get('cod_municipio'))
			ficha.save()
			return redirect(reverse('nueva_ficha_3', kwargs={'cod_censo': ficha.cod_censo}))



	except Exception as e:
		print e

	return render(request, 'nueva_ficha_2.html', {'form1': form1})




def nueva_ficha_3(request, id_censo):

	ficha = FichaCenso.objects.get(pk=id_censo)

	form1 = FichaCensoForm()	

	return render(request, 'nueva_ficha_3.html', {'form1': form1})	


def nueva_ficha_4(request, id_censo):
	ficha = FichaCenso.objects.get(pk=id_censo)
	form1 = FichaCensoForm()	

	return render(request, 'nueva_ficha_4.html', {'form1': form1})	

def nueva_ficha_5(request, id_censo):
	ficha = FichaCenso.objects.get(pk=id_censo)
	form1 = FichaCensoForm()	

	return render(request, 'nueva_ficha_5.html', {'form1': form1})	

def nueva_ficha_6(request, id_censo):
	ficha = FichaCenso.objects.get(pk=id_censo)
	form1 = FichaCensoForm()	

	return render(request, 'nueva_ficha_6.html', {'form1': form1})	


def nueva_ficha_7(request, id_censo):
	ficha = FichaCenso.objects.get(pk=id_censo)
	form1 = FichaCensoForm()	

	return render(request, 'nueva_ficha_7.html', {'form1': form1})	


def nueva_ficha_8(request):
	form1 = FichaCensoForm()
	try:
		if request.POST:
			censo = FichaCenso()
			censo.hijos = None if request.POST.get('hijos') == '' else request.POST.get('hijos')
			censo.cantidad_hijos = None if request.POST.get('cantidad_hijos') == '' else request.POST.get('cantidad_hijos')

			censo.save()

			return redirect('ingresar_hijos')

		pass
	except Exception as e:
		raise e


	return render(request, 'nueva_ficha_8.html', {'form1': form1})	



def ingresar_hijos(request):
	formFicha = FichaCensoForm()
	formHijos = IngresarHijosForm()

	
	ctx = {
		'formFicha': formFicha,
		'formHijos': formHijos,
		
	}

	return render(request, 'ingresar_hijos.html', ctx)	



import json
def ajax(request):
	if request.is_ajax():
		cod_departament_nacimiento = request.GET['cod_departament_nacimiento']
		data = list(Municipios.objects.values('cod_municipio', 'desc_municipio').filter(cod_departamento=cod_departament_nacimiento))
		return HttpResponse(json.dumps(data), content_type='application/json')


def ajax2(request):
	if request.is_ajax():
		cod_departament_domicilio = request.GET['cod_departament_domicilio']
		data = list(Municipios.objects.values('cod_municipio', 'desc_municipio').filter(cod_departamento=cod_departament_domicilio))
		return HttpResponse(json.dumps(data), content_type='application/json')