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
		if request.POST:
			form1 = FichaCensoForm()
			ficha = FichaCenso.objects.get(cod_censo=cod_censo)
			ficha.nivel_educativo = None if request.POST.get('nivel_educativo') == '' else request.POST.get('nivel_educativo')
			ficha.cod_profesion_oficio = ProfesionOficio.objects.get(pk=request.POST.get('cod_profesion_oficio'))
			ficha.cod_departament_domicilio = Departamentos.objects.get(pk=request.POST.get('cod_departament_domicilio'))
			ficha.cod_municipio_domicilio = Municipios.objects.get(pk=request.POST.get('cod_municipio'))
		
			ficha.save()
		return redirect(reverse('nueva_ficha_3', kwargs={'cod_censo': ficha.cod_censo}))
		
	except Exception as e:
		print e

	return render(request, 'nueva_ficha_2.html', {'form1': form1})




def nueva_ficha_3(request, cod_censo):

	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)
			
			ficha = FichaCenso.objects.get(cod_censo=cod_censo)
			ficha.barrio_o_colonia_domicilio = None if request.POST.get('barrio_o_colonia_domicilio') == '' else request.POST.get('barrio_o_colonia_domicilio')
			ficha.calle_domicilio = None if request.POST.get('calle_domicilio') == '' else request.POST.get('calle_domicilio')
			ficha.avenida_domicilio = None if request.POST.get('avenida_domicilio') == '' else request.POST.get('avenida_domicilio')
			ficha.bloque_domicilio = None if request.POST.get('bloque_domicilio') == '' else request.POST.get('bloque_domicilio')
			ficha.no_casa_domicilio = None if request.POST.get('no_casa_domicilio') == '' else request.POST.get('no_casa_domicilio')
			ficha.color_domicilio = None if request.POST.get('color_domicilio') == '' else request.POST.get('color_domicilio')
			ficha.punto_referencia_domicilio = None if request.POST.get('punto_referencia_domicilio') == '' else request.POST.get('punto_referencia_domicilio')

			ficha.telefono_fijo_domicilio = None if request.POST.get('telefono_fijo_domicilio') == '' else request.POST.get('telefono_fijo_domicilio')
			ficha.telefono_otro_domicilio = None if request.POST.get('telefono_otro_domicilio') == '' else request.POST.get('telefono_otro_domicilio')
			ficha.celular_domicilio = None if request.POST.get('celular_domicilio') == '' else request.POST.get('celular_domicilio')
			ficha.correo_electronico_domicilio = None if request.POST.get('correo_electronico_domicilio') == '' else request.POST.get('correo_electronico_domicilio')		
			
			ficha.save()
			return redirect(reverse('nueva_ficha_4', kwargs={'cod_censo': ficha.cod_censo}))
	except Exception as e:
		print e	

	return render(request, 'nueva_ficha_3.html', {'form1': form1})	



def nueva_ficha_4(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)
			# None if request.POST.get('') == '' else request.POST.get('')

		ficha = FichaCenso.objects.get(cod_censo=cod_censo)
		ficha.conyuge = None if request.POST.get('conyuge') == '' else request.POST.get('conyuge')
		ficha.identidad_conyuge = None if request.POST.get('identidad_conyuge') == '' else request.POST.get('identidad_conyuge')
		ficha.nombres_conyuge = None if request.POST.get('nombres_conyuge') == '' else request.POST.get('nombres_conyuge')
		ficha.primer_apellido_conyuge = None if request.POST.get('primer_apellido_conyuge') == '' else request.POST.get('primer_apellido_conyuge')
		ficha.segundo_apellido_conyuge = None if request.POST.get('segundo_apellido_conyuge') == '' else request.POST.get('segundo_apellido_conyuge')

		ficha.save()
		return redirect(reverse('nueva_ficha_5', kwargs={'cod_censo': ficha.cod_censo}))
	except Exception as e:
		print e	

	return render(request, 'nueva_ficha_4.html', {'form1': form1})	

def nueva_ficha_5(request, cod_censo):

	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)
			# None if request.POST.get('') == '' else request.POST.get('')

		ficha = FichaCenso.objects.get(cod_censo=cod_censo)

		# trabaja_actualmente = models.NullBooleanField(db_column='TrabajaActualmente')  # Field name made lowercase.
		# lugar_de_trabajo = models.CharField(db_column='LugarTrabajo', max_length=1, blank=True, null=True)  # Field name made lowercase.
		# tipo_contratacion = models.CharField(db_column='TipoContratacion', max_length=1, blank=True, null=True)  # Field name made lowercase.
		# antiguedad_meses = models.IntegerField(db_column='AntiguedadMeses', blank=True, null=True)  # Field name made lowercase.
		# nombre_empresa = models.CharField(db_column='NombreEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.   
		# departamento_o_seccion = models.CharField(db_column='DeptoSeccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
		# cargo = models.CharField(db_column='Cargo', max_length=50, blank=True, null=True)  # Field name made lowercase.
		# cod_departamento_empresa = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDepartamentEmpresa', related_name='CodDepartamentEmpresa_Deptos', blank=True, null=True)  # Field name made lowercase.
		# cod_municipio_empresa = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='CodMunicipioEmpresa', related_name='CodMunicipioEmpresa_Muni', blank=True, null=True)  # Field name made lowercase.
		# barrio_o_colonia_empresa = models.CharField(db_column='BarrioColoniaDEmpresa', max_length=100, blank=True, null=True)  # Field name made lowercase.	
		# calle_empresa = models.CharField

		ficha.save()
		return redirect(reverse('nueva_ficha_6', kwargs={'cod_censo': ficha.cod_censo}))
	except Exception as e:
		print e		

	return render(request, 'nueva_ficha_5.html', {'form1': form1})	

def nueva_ficha_6(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)
		

		ficha = FichaCenso.objects.get(cod_censo=cod_censo)
		ficha.avenida_empresa = None if request.POST.get('') == 'avenida_empresa' else request.POST.get('avenida_empresa')
		ficha.bloque_empresa = None if request.POST.get('bloque_empresa') == '' else request.POST.get('bloque_empresa')
		ficha.no_casa_empresa = None if request.POST.get('no_casa_empresa') == '' else request.POST.get('no_casa_empresa')
		ficha.color_empresa = None if request.POST.get('color_empresa') == '' else request.POST.get('color_empresa')
		ficha.etapa_empresa = None if request.POST.get('etapa_empresa') == '' else request.POST.get('etapa_empresa')
		ficha.punto_referencia_empresa = None if request.POST.get('punto_referencia_empresa') == '' else request.POST.get('punto_referencia_empresa')
		ficha.telefono_fijo_empresa = None if request.POST.get('telefono_fijo_empresa') == '' else request.POST.get('telefono_fijo_empresa')
		ficha.telefono_otro_empresa = None if request.POST.get('telefono_otro_empresa') == '' else request.POST.get('telefono_otro_empresa')
		ficha.celular_empresa = None if request.POST.get('celular_empresa') == '' else request.POST.get('celular_empresa')
		ficha.correo_electronico_empresa = None if request.POST.get('correo_electronico_empresa') == '' else request.POST.get('correo_electronico_empresa')

		ficha.save()
		return redirect(reverse('nueva_ficha_7', kwargs={'cod_censo': ficha.cod_censo}))
	except Exception as e:
		print e	

	return render(request, 'nueva_ficha_6.html', {'form1': form1})		


def nueva_ficha_7(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)
			
		ficha = FichaCenso.objects.get(cod_censo=cod_censo)
		ficha.negocio_propio = None if request.POST.get('negocio_propio') == '' else request.POST.get('negocio_propio')
		ficha.negocio_especificar = None if request.POST.get('negocio_especificar') == '' else request.POST.get('negocio_especificar')
		ficha.num_empleados = None if request.POST.get('num_empleados') == '' else request.POST.get('num_empleados')
		ficha.antiguedad_negocio_meses = None if request.POST.get('antiguedad_negocio_meses') == '' else request.POST.get('antiguedad_negocio_meses')
		ficha.rubro_negocio = None if request.POST.get('rubro_negocio') == '' else request.POST.get('rubro_negocio')
		ficha.otros_ingresos = None if request.POST.get('otros_ingresos') == '' else request.POST.get('otros_ingresos')
		ficha.cantidad_promedio = None if request.POST.get('cantidad_promedio') == '' else request.POST.get('cantidad_promedio')
		ficha.nivel_ingreso = None if request.POST.get('nivel_ingreso') == '' else request.POST.get('nivel_ingreso')
		ficha.trabaja_conyuge = None if request.POST.get('trabaja_conyuge') == '' else request.POST.get('trabaja_conyuge')
		ficha.nivel_ingreso_conyuge = None if request.POST.get('nivel_ingreso_conyuge') == '' else request.POST.get('nivel_ingreso_conyuge')
		ficha.save()
		return redirect(reverse('nueva_ficha_8', kwargs={'cod_censo': ficha.cod_censo}))
	except Exception as e:
		print e		
	return render(request, 'nueva_ficha_7.html', {'form1': form1})	


def nueva_ficha_8(request, cod_censo):

	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)
			# None if request.POST.get('') == '' else request.POST.get('')

		ficha = FichaCenso.objects.get(cod_censo=cod_censo)
		ficha.hijos = None if request.POST.get('hijos') == '' else request.POST.get('hijos')
		ficha.cantidad_hijos = None if request.POST.get('cantidad_hijos') == '' else request.POST.get('cantidad_hijos')
	
		ficha.save()
		return redirect(reverse('ingresar_hijos', kwargs={'cod_censo': ficha.cod_censo}))
	except Exception as e:
		print e	


	return render(request, 'nueva_ficha_8.html', {'form1': form1})	



def ingresar_hijos(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)

	try:
		if request.method == 'GET':
			form1 = FichaCensoForm(instance=ficha)
		else:
			form1 = FichaCensoForm(request.POST, instance=ficha)
			# None if request.POST.get('') == '' else request.POST.get('')

		
		# return redirect(reverse('nueva_ficha_9', kwargs={'cod_censo': ficha.cod_censo}))
	except Exception as e:
		print e	
	return render(request, 'ingresar_hijos.html', {})




def nueva_ficha_9(request):
	# ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm()
	else:
		form1 = FichaCensoForm()
	
	return render(request, 'nueva_ficha_9.html', {'form1': form1})

def nueva_ficha_10(request):
	# ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm()
	else:
		form1 = FichaCensoForm()
	
	return render(request, 'nueva_ficha_10.html', {'form1': form1})		


def nueva_ficha_11(request):
	# ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm()
	else:
		form1 = FichaCensoForm()
	
	return render(request, 'nueva_ficha_11.html', {'form1': form1})	


def nueva_ficha_12(request):
	# ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm()
	else:
		form1 = FichaCensoForm()
	
	return render(request, 'nueva_ficha_12.html', {'form1': form1})


def nueva_ficha_13(request):
	# ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm()
	else:
		form1 = FichaCensoForm()
	
	return render(request, 'nueva_ficha_13.html', {'form1': form1})


def nueva_ficha_14(request):
	# ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm()
	else:
		form1 = FichaCensoForm()
	
	return render(request, 'nueva_ficha_14.html', {'form1': form1})			


def nueva_ficha_15(request):
	# ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm()
	else:
		form1 = FichaCensoForm()
	
	return render(request, 'nueva_ficha_15.html', {'form1': form1})	



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


def ajax3(request):
	if request.is_ajax():
		cod_departamento_empresa = request.GET['cod_departamento_empresa']
		data = list(Municipios.objects.values('cod_municipio', 'desc_municipio').filter(cod_departamento=cod_departamento_empresa))
		return HttpResponse(json.dumps(data), content_type='application/json')	

def ajax_municipioEncuesta(request):
	if request.is_ajax():
		departamento_encuesta = request.GET['departamento_encuesta']
		data = list(Municipios.objects.values('cod_municipio', 'desc_municipio').filter(cod_departamento=departamento_encuesta))
		return HttpResponse(json.dumps(data), content_type='application/json')

