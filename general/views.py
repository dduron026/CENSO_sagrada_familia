from django.shortcuts import render, redirect
from django.db import transaction, IntegrityError

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

def listado_ficha(request):
	lista = FichaCenso.objects.all().order_by('cod_censo')

	return render(request, 'listado_ficha.html', {'lista': lista})



@transaction.atomic
def nueva_ficha(request):
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
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
				ficha.apellido_de_casada = None if request.POST.get('apellido_de_casada') == '' else request.POST.get('apellido_de_casada')
				ficha.cod_estado = Estados.objects.get(pk=0)
				ficha.cod_vista = 2
				
				ficha.save()
				return redirect(reverse('nueva_ficha_2', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'
		
	return render(request, 'nueva_ficha.html', {'form1': form1})


def nueva_ficha_2(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.nivel_educativo = None if request.POST.get('nivel_educativo') == '' else request.POST.get('nivel_educativo')
				ficha.cod_profesion_oficio = ProfesionOficio.objects.get(pk=request.POST.get('cod_profesion_oficio'))
				ficha.cod_departament_domicilio = Departamentos.objects.get(pk=request.POST.get('cod_departament_domicilio'))
				ficha.cod_municipio_domicilio = Municipios.objects.get(pk=request.POST.get('cod_municipio'))
				ficha.cod_vista = 3
				ficha.save()
				return redirect(reverse('nueva_ficha_3', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_2.html', {'form1': form1})


def nueva_ficha_3(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
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
				ficha.cod_vista = 4
				ficha.save()
				return redirect(reverse('nueva_ficha_4', kwargs={'cod_censo': ficha.cod_censo}))
		except Exception as e:
			mensaje = 'error'

	return render(request, 'nueva_ficha_3.html', {'form1': form1})	



def nueva_ficha_4(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.conyuge = None if request.POST.get('conyuge') == '' else request.POST.get('conyuge')
				ficha.identidad_conyuge = None if request.POST.get('identidad_conyuge') == '' else request.POST.get('identidad_conyuge')
				ficha.nombres_conyuge = None if request.POST.get('nombres_conyuge') == '' else request.POST.get('nombres_conyuge')
				ficha.primer_apellido_conyuge = None if request.POST.get('primer_apellido_conyuge') == '' else request.POST.get('primer_apellido_conyuge')
				ficha.segundo_apellido_conyuge = None if request.POST.get('segundo_apellido_conyuge') == '' else request.POST.get('segundo_apellido_conyuge')
				ficha.cod_vista = 5
				ficha.save()
				return redirect(reverse('nueva_ficha_5', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_4.html', {'form1': form1})




def nueva_ficha_5(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		if request.POST['trabaja_actualmente'] == 'False':			
			return redirect(reverse('nueva_ficha_7', kwargs={'cod_censo': ficha.cod_censo}))
		else:
			try:
				with transaction.atomic():
					ficha = FichaCenso.objects.get(cod_censo=cod_censo)
					ficha.trabaja_actualmente = None if request.POST.get('trabaja_actualmente') == '' else request.POST.get('trabaja_actualmente')
					ficha.lugar_de_trabajo = None if request.POST.get('lugar_de_trabajo') == '' else request.POST.get('lugar_de_trabajo')
					ficha.tipo_contratacion = None if request.POST.get('tipo_contratacion') == '' else request.POST.get('tipo_contratacion')
					ficha.antiguedad_meses = None if request.POST.get('antiguedad_meses') == '' else request.POST.get('antiguedad_meses')
					ficha.nombre_empresa = None if request.POST.get('nombre_empresa') == '' else request.POST.get('nombre_empresa')
					ficha.departamento_o_seccion = None if request.POST.get('departamento_o_seccion') == '' else request.POST.get('departamento_o_seccion')
					ficha.cargo = None if request.POST.get('cargo') == '' else request.POST.get('cargo')
					ficha.cod_departamento_empresa = Departamentos.objects.get(pk=request.POST.get('cod_departamento_empresa'))
					ficha.cod_municipio_empresa = Municipios.objects.get(pk=request.POST.get('cod_municipio'))
					ficha.barrio_o_colonia_empresa = None if request.POST.get('barrio_o_colonia_empresa') == '' else request.POST.get('barrio_o_colonia_empresa')
					ficha.calle_empresa = None if request.POST.get('calle_empresa') == '' else request.POST.get('calle_empresa')
					ficha.cod_vista = 6
					ficha.save()
					return redirect(reverse('nueva_ficha_6', kwargs={'cod_censo': ficha.cod_censo}))
			except Exception as e:
				mensaje = 'error'	

	return render(request, 'nueva_ficha_5.html', {'form1': form1}) 	


		

def nueva_ficha_6(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
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
				ficha.cod_vista = 7
				ficha.save()
				return redirect(reverse('nueva_ficha_7', kwargs={'cod_censo': ficha.cod_censo}))			
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_6.html', {'form1': form1}) 			


def nueva_ficha_7(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
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
				ficha.cod_vista = 8
				ficha.save()
				return redirect(reverse('nueva_ficha_8', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_7.html', {'form1': form1}) 				



def nueva_ficha_8(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.hijos = None if request.POST.get('hijos') == '' else request.POST.get('hijos')
				ficha.cantidad_de_hijos = None if request.POST.get('cantidad_de_hijos') == '' else request.POST.get('cantidad_de_hijos')
				ficha.cod_vista = 9
				ficha.save()
				return redirect(reverse('ingresar_hijos', kwargs={'cod_censo': ficha.cod_censo, 'cantidad': ficha.cantidad_de_hijos}))				
		except Exception as e:
			raise e
	return render(request, 'nueva_ficha_8.html', {'form1': form1})	



def ingresar_hijos(request, cod_censo, cantidad):
	ficha = FichaCenso.objects.get(pk=cod_censo)	
	form1 = FichaCensoForm()	
	hijos = HijosForm()
	
	if request.POST:
		try:
			with transaction.atomic():

				num_hijo = request.POST.getlist('num_hijo[]')
				nombre_hijo = request.POST.getlist('nombre_hijo[]')
				edad = request.POST.getlist('edad[]')
				estudia_trabaja = request.POST.getlist('estudia_trabaja[]')
				nivel_estudio = request.POST.getlist('nivel_estudio[]')
				institucion_estudio = request.POST.getlist('institucion_estudio[]')
				institucion_trabajo = request.POST.getlist('institucion_trabajo[]')
				sueldo = request.POST.getlist('sueldo[]')
				
				counter = 0
				for x in nombre_hijo: #elijo un campo del modelo
					
					ingresoHijo = Hijos()
					ficha = FichaCenso.objects.get(cod_censo=cod_censo)
					ingresoHijo.cod_censo = FichaCenso.objects.get(pk=cod_censo)
					ingresoHijo.num_hijo = None if num_hijo[counter] == '' else num_hijo[counter]
					ingresoHijo.nombre_hijo = None if nombre_hijo[counter] == '' else nombre_hijo[counter]
					ingresoHijo.edad = None if edad[counter] == '' else edad[counter]
					ingresoHijo.estudia_trabaja = None if estudia_trabaja[counter] == '' else estudia_trabaja[counter]
					ingresoHijo.nivel_estudio = None if nivel_estudio[counter] == '' else nivel_estudio[counter]
					ingresoHijo.institucion_estudio = None if institucion_estudio[counter] == '' else institucion_estudio[counter]
					ingresoHijo.institucion_trabajo = None if institucion_trabajo[counter] == '' else institucion_trabajo[counter]
					ingresoHijo.sueldo = None if sueldo[counter] == '' else sueldo[counter]	
					ficha.cod_vista = 10
					ingresoHijo.save()
					counter += 1				
			
				return redirect(reverse('nueva_ficha_9', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			raise e
			mensaje = 'error'
	ctx = {	'form1': form1,
			'hijos': hijos,
			'cantidad': range(0,int(cantidad)),
		}
	return render(request, 'ingresar_hijos.html', ctx) 

	



def nueva_ficha_9(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.hijos_afiliados = None if request.POST.get('hijos_afiliados') == '' else request.POST.get('hijos_afiliados')
				ficha.papel_casa = None if request.POST.get('papel_casa') == '' else request.POST.get('papel_casa')
				ficha.vehiculo = None if request.POST.get('vehiculo') == '' else request.POST.get('vehiculo')
				ficha.cantidad_vehiculos = None if request.POST.get('cantidad_vehiculos') == '' else request.POST.get('cantidad_vehiculos')
				ficha.tipo_casa = None if request.POST.get('tipo_casa') == '' else request.POST.get('tipo_casa')
				ficha.numero_habitaciones = None if request.POST.get('numero_habitaciones') == '' else request.POST.get('numero_habitaciones')
				ficha.numero_televisores = None if request.POST.get('numero_televisores') == '' else request.POST.get('numero_televisores')
				ficha.cantidad_personas = None if request.POST.get('cantidad_personas') == '' else request.POST.get('cantidad_personas')
				ficha.numero_ninos = None if request.POST.get('numero_ninos') == '' else request.POST.get('numero_ninos')
				ficha.numero_adolescentes = None if request.POST.get('numero_adolescentes') == '' else request.POST.get('numero_adolescentes')
				ficha.cod_vista = 11
				ficha.save()
				return redirect(reverse('nueva_ficha_10', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_9.html', {'form1': form1}) 



def nueva_ficha_10(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.mayores_edad = None if request.POST.get('mayores_edad') == '' else request.POST.get('mayores_edad')
				ficha.mayores_a_60 = None if request.POST.get('mayores_a_60') == '' else request.POST.get('mayores_a_60')
				ficha.anos_afiliacion = None if request.POST.get('anos_afiliacion') == '' else request.POST.get('anos_afiliacion')
				ficha.tipo_afiliado = None if request.POST.get('tipo_afiliado') == '' else request.POST.get('tipo_afiliado')
				ficha.cod_filial_afiliacion = Filiales.objects.get(pk=request.POST.get('cod_filial_afiliacion'))
				ficha.cod_filial_visita = Filiales.objects.get(pk=request.POST.get('cod_filial_visita'))
				ficha.cursos_capacitaciones = None if request.POST.get('cursos_capacitaciones') == '' else request.POST.get('cursos_capacitaciones')
				ficha.asambleas_sectoriales = None if request.POST.get('asambleas_sectoriales') == '' else request.POST.get('asambleas_sectoriales')
				ficha.cod_vista = 12
				ficha.save()
				return redirect(reverse('nueva_ficha_11', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_10.html', {'form1': form1}) 


def nueva_ficha_11(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	prestamos = PrestamosForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.prestamos_otros = None if request.POST.get('prestamos_otros') == '' else request.POST.get('prestamos_otros')
				ficha.tipo_institucion_prestamos = None if request.POST.get('tipo_institucion_prestamos') == '' else request.POST.get('tipo_institucion_prestamos')
				ficha.cod_vista = 13
				ficha.save()

				institucion = request.POST.getlist('institucion[]')
				tipo_prestamos = request.POST.getlist('tipo_prestamos[]')
				moneda = request.POST.getlist('moneda[]')
				tasa = request.POST.getlist('tasa[]')
				monto_original = request.POST.getlist('monto_original[]')
				plazo_meses = request.POST.getlist('plazo_meses[]')

				counter = 0

				for x in institucion:
					prestamo = Prestamos()
					prestamo.cod_censo = FichaCenso.objects.get(pk=cod_censo)
					prestamo.institucion = None if institucion[counter] == '' else institucion[counter]
					prestamo.tipo_prestamos = None if tipo_prestamos[counter] == '' else tipo_prestamos[counter]
					prestamo.moneda = None if moneda[counter] == '' else moneda[counter]
					prestamo.tasa = None if tasa[counter] == '' else tasa[counter]
					prestamo.monto_original = None if monto_original[counter] == '' else monto_original[counter]
					prestamo.plazo_meses = None if plazo_meses[counter] == '' else plazo_meses[counter]

					prestamo.save()
					counter += 1

				return redirect(reverse('nueva_ficha_12', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			raise e
	return render(request, 'nueva_ficha_11.html', {'form1': form1, 'prestamos': prestamos})




def nueva_ficha_12(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.destino_pendiente_pago = None if request.POST.get('destino_pendiente_pago') == '' else request.POST.get('destino_pendiente_pago')
				ficha.otros_destino = None if request.POST.get('otros_destino') == '' else request.POST.get('otros_destino')
				ficha.cuenta_ahorro_otro = None if request.POST.get('cuenta_ahorro_otro') == '' else request.POST.get('cuenta_ahorro_otro')
				ficha.nombre_institucion_ahorro = None if request.POST.get('nombre_institucion_ahorro') == '' else request.POST.get('nombre_institucion_ahorro')
				ficha.tipo_cuenta_ahorro = None if request.POST.get('tipo_cuenta_ahorro') == '' else request.POST.get('tipo_cuenta_ahorro')
				ficha.otros_tipo_cuenta = None if request.POST.get('otros_tipo_cuenta') == '' else request.POST.get('otros_tipo_cuenta')
				ficha.tarjeta_credito = None if request.POST.get('tarjeta_credito') == '' else request.POST.get('tarjeta_credito')
				ficha.cantidad_tarjetas = None if request.POST.get('cantidad_tarjetas') == '' else request.POST.get('cantidad_tarjetas')
				ficha.nombre_institucion_tarjeta = None if request.POST.get('nombre_institucion_tarjeta') == '' else request.POST.get('nombre_institucion_tarjeta')
				ficha.tipo_tarjeta = None if request.POST.get('tipo_tarjeta') == '' else request.POST.get('tipo_tarjeta')
				ficha.cod_vista = 14
				ficha.save()
				return redirect(reverse('nueva_ficha_13', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_12.html', {'form1': form1})

	


def nueva_ficha_13(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.limite_tarjeta = None if request.POST.get('limite_tarjeta') == '' else request.POST.get('limite_tarjeta')
				ficha.tipo_compra_casa = None if request.POST.get('tipo_compra_casa') == '' else request.POST.get('tipo_compra_casa')
				ficha.cuota_casa_mensual = None if request.POST.get('cuota_casa_mensual') == '' else request.POST.get('cuota_casa_mensual')
				ficha.nombre_institucion_casa = None if request.POST.get('nombre_institucion_casa') == '' else request.POST.get('nombre_institucion_casa')
				ficha.sistema_cable = None if request.POST.get('sistema_cable') == '' else request.POST.get('sistema_cable')
				ficha.internet = None if request.POST.get('internet') == '' else request.POST.get('internet')
				ficha.cod_vista = 15
				ficha.save()
				return redirect(reverse('nueva_ficha_14', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_13.html', {'form1': form1})


def nueva_ficha_14(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.remesas_extrajero = None if request.POST.get('remesas_extrajero') == '' else request.POST.get('remesas_extrajero')
				ficha.pais_remesas = None if request.POST.get('pais_remesas') == '' else request.POST.get('pais_remesas')
				ficha.ciudad_remesas = None if request.POST.get('ciudad_remesas') == '' else request.POST.get('ciudad_remesas')	
				ficha.quien_envia = None if request.POST.get('quien_envia') == '' else request.POST.get('quien_envia')	
				ficha.uso_remesas = None if request.POST.get('uso_remesas') == '' else request.POST.get('uso_remesas')	
				ficha.empresa_remesas = None if request.POST.get('empresa_remesas') == '' else request.POST.get('empresa_remesas')	
				ficha.cada_cuanto_recibe = None if request.POST.get('cada_cuanto_recibe') == '' else request.POST.get('cada_cuanto_recibe')	
				ficha.promedio_remesas = None if request.POST.get('promedio_remesas') == '' else request.POST.get('promedio_remesas')	
				ficha.cod_vista = 16
				ficha.save()
				return redirect(reverse('nueva_ficha_15', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'nueva_ficha_14.html', {'form1': form1})





def nueva_ficha_15(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	form1 = FichaCensoForm()
	if request.POST:
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.fecha_censo = None if request.POST.get('fecha_censo') == '' else request.POST.get('fecha_censo')
				ficha.cod_usuario = None if request.POST.get('cod_usuario') == '' else request.POST.get('cod_usuario')
				ficha.departamento_encuesta = Departamentos.objects.get(pk=request.POST.get('departamento_encuesta')) #el atributo 'name' del elemento <select>
				ficha.municipio_encuesta = Municipios.objects.get(pk=request.POST.get('cod_municipio')) #el atributo 'name' del elemento <select>
				ficha.filial_encuesta = Filiales.objects.get(pk=request.POST.get('filial_encuesta'))
				ficha.cod_estado = Estados.objects.get(pk=1)
				ficha.cod_vista = 17
				ficha.save()
				return redirect(reverse('menu_principal', kwargs={}))			
		except Exception as e:
			raise e
	return render(request, 'nueva_ficha_15.html', {'form1': form1})


# ***************************************************EDITAR FICHA*******************************************************************************************************


def editar_ficha_1(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)

	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
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
				ficha.apellido_de_casada = None if request.POST.get('apellido_de_casada') == '' else request.POST.get('apellido_de_casada')
				ficha.cod_estado = Estados.objects.get(pk=0)
				ficha.cod_vista = 2
				
				ficha.save()
				return redirect(reverse('editar_ficha_2', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			raise e
		
	return render(request, 'editar/editar_ficha_1.html', {'form1': form1})


def editar_ficha_2(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.nivel_educativo = None if request.POST.get('nivel_educativo') == '' else request.POST.get('nivel_educativo')
				ficha.cod_profesion_oficio = ProfesionOficio.objects.get(pk=request.POST.get('cod_profesion_oficio'))
				ficha.cod_departament_domicilio = Departamentos.objects.get(pk=request.POST.get('cod_departament_domicilio'))
				ficha.cod_municipio_domicilio = Municipios.objects.get(pk=request.POST.get('cod_municipio'))
				ficha.cod_vista = 3		
				ficha.save()
				return redirect(reverse('editar_ficha_3', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'
	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_2.html', ctx)	


def editar_ficha_3(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
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
				ficha.cod_vista = 4
	
				ficha.save()
				return redirect(reverse('editar_ficha_4', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'
	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_3.html', ctx)	




def editar_ficha_4(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.conyuge = None if request.POST.get('conyuge') == '' else request.POST.get('conyuge')
				ficha.identidad_conyuge = None if request.POST.get('identidad_conyuge') == '' else request.POST.get('identidad_conyuge')
				ficha.nombres_conyuge = None if request.POST.get('nombres_conyuge') == '' else request.POST.get('nombres_conyuge')
				ficha.primer_apellido_conyuge = None if request.POST.get('primer_apellido_conyuge') == '' else request.POST.get('primer_apellido_conyuge')
				ficha.segundo_apellido_conyuge = None if request.POST.get('segundo_apellido_conyuge') == '' else request.POST.get('segundo_apellido_conyuge')
				ficha.cod_vista = 5
	
				ficha.save()
				return redirect(reverse('editar_ficha_5', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'
	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_4.html', ctx)	





def editar_ficha_5(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.conyuge = None if request.POST.get('conyuge') == '' else request.POST.get('conyuge')
				ficha.identidad_conyuge = None if request.POST.get('identidad_conyuge') == '' else request.POST.get('identidad_conyuge')
				ficha.nombres_conyuge = None if request.POST.get('nombres_conyuge') == '' else request.POST.get('nombres_conyuge')
				ficha.primer_apellido_conyuge = None if request.POST.get('primer_apellido_conyuge') == '' else request.POST.get('primer_apellido_conyuge')
				ficha.segundo_apellido_conyuge = None if request.POST.get('segundo_apellido_conyuge') == '' else request.POST.get('segundo_apellido_conyuge')
				ficha.cod_vista = 6
	
				ficha.save()
				return redirect(reverse('editar_ficha_6', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'
	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_5.html', ctx )



def editar_ficha_6(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
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
				ficha.cod_vista = 7
	
				ficha.save()
				return redirect(reverse('editar_ficha_7', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_6.html', ctx)		



def editar_ficha_7(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
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
				ficha.cod_vista = 8
	
				ficha.save()
				return redirect(reverse('editar_ficha_8', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_7.html', ctx )



def editar_ficha_8(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.hijos = None if request.POST.get('hijos') == '' else request.POST.get('hijos')
				ficha.cantidad_de_hijos = None if request.POST.get('cantidad_de_hijos') == '' else request.POST.get('cantidad_de_hijos')
				ficha.cod_vista = 9
	
				ficha.save()
				return redirect(reverse('editar_hijos', kwargs={'cod_censo': ficha.cod_censo, 'cantidad': ficha.cantidad_de_hijos}))
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_8.html', ctx )		



def editar_hijos(request, cod_censo, cantidad):
	
	x = Hijos.objects.filter(cod_censo=cod_censo)
	ficha = FichaCenso.objects.get(pk=cod_censo)	
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
		hijos = []
		for hijo in x:
			hijo = HijosForm(instance=hijo)
			hijos.append(hijo)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)

		try:
			with transaction.atomic():

				num_hijo = request.POST.getlist('num_hijo[]')
				nombre_hijo = request.POST.getlist('nombre_hijo[]')
				edad = request.POST.getlist('edad[]')
				estudia_trabaja = request.POST.getlist('estudia_trabaja[]')
				nivel_estudio = request.POST.getlist('nivel_estudio[]')
				institucion_estudio = request.POST.getlist('institucion_estudio[]')
				institucion_trabajo = request.POST.getlist('institucion_trabajo[]')
				sueldo = request.POST.getlist('sueldo[]')
				
				hijo = Hijos.objects.filter(cod_censo=cod_censo).delete()
				# borro los registros y los vuelvo a crear
				counter = 0
				for x in nombre_hijo:				
					
					hijo = Hijos()
					hijo.cod_censo = FichaCenso.objects.get(pk=cod_censo)
					hijo.num_hijo = None if num_hijo[counter] == '' else num_hijo[counter]
					hijo.nombre_hijo = None if nombre_hijo[counter] == '' else nombre_hijo[counter]
					hijo.edad = None if edad[counter] == '' else edad[counter]
					hijo.estudia_trabaja = None if estudia_trabaja[counter] == '' else estudia_trabaja[counter]
					hijo.nivel_estudio = None if nivel_estudio[counter] == '' else nivel_estudio[counter]
					hijo.institucion_estudio = None if institucion_estudio[counter] == '' else institucion_estudio[counter]
					hijo.institucion_trabajo = None if institucion_trabajo[counter] == '' else institucion_trabajo[counter]
					hijo.sueldo = None if sueldo[counter] == '' else sueldo[counter]	
					ficha.cod_vista = 10
					hijo.save()
					counter += 1							
				return redirect(reverse('editar_ficha_9', kwargs={'cod_censo': ficha.cod_censo}))		
		except Exception as e:
			mensaje = 'error'
			
	ctx = {	'form1': form1,
			'ficha': ficha,
			'hijos': hijos,
			'cantidad': range(0,int(cantidad)),
		}
	return render(request, 'editar/editar_hijos.html', ctx)



def editar_ficha_9(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.hijos_afiliados = None if request.POST.get('hijos_afiliados') == '' else request.POST.get('hijos_afiliados')
				ficha.papel_casa = None if request.POST.get('papel_casa') == '' else request.POST.get('papel_casa')
				ficha.vehiculo = None if request.POST.get('vehiculo') == '' else request.POST.get('vehiculo')
				ficha.cantidad_vehiculos = None if request.POST.get('cantidad_vehiculos') == '' else request.POST.get('cantidad_vehiculos')
				ficha.tipo_casa = None if request.POST.get('tipo_casa') == '' else request.POST.get('tipo_casa')
				ficha.numero_habitaciones = None if request.POST.get('numero_habitaciones') == '' else request.POST.get('numero_habitaciones')
				ficha.numero_televisores = None if request.POST.get('numero_televisores') == '' else request.POST.get('numero_televisores')
				ficha.cantidad_personas = None if request.POST.get('cantidad_personas') == '' else request.POST.get('cantidad_personas')
				ficha.numero_ninos = None if request.POST.get('numero_ninos') == '' else request.POST.get('numero_ninos')
				ficha.numero_adolescentes = None if request.POST.get('numero_adolescentes') == '' else request.POST.get('numero_adolescentes')
				ficha.cod_vista = 11
	
				ficha.save()
				return redirect(reverse('editar_ficha_10', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_9.html', ctx )



def editar_ficha_10(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.mayores_edad = None if request.POST.get('mayores_edad') == '' else request.POST.get('mayores_edad')
				ficha.mayores_a_60 = None if request.POST.get('mayores_a_60') == '' else request.POST.get('mayores_a_60')
				ficha.anos_afiliacion = None if request.POST.get('anos_afiliacion') == '' else request.POST.get('anos_afiliacion')
				ficha.tipo_afiliado = None if request.POST.get('tipo_afiliado') == '' else request.POST.get('tipo_afiliado')
				ficha.cod_filial_afiliacion = Filiales.objects.get(pk=request.POST.get('cod_filial_afiliacion'))
				ficha.cod_filial_visita = Filiales.objects.get(pk=request.POST.get('cod_filial_visita'))
				ficha.cursos_capacitaciones = None if request.POST.get('cursos_capacitaciones') == '' else request.POST.get('cursos_capacitaciones')
				ficha.asambleas_sectoriales = None if request.POST.get('asambleas_sectoriales') == '' else request.POST.get('asambleas_sectoriales')
				ficha.cod_vista = 12				
	
				ficha.save()
				return redirect(reverse('editar_ficha_11', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			raise e

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_10.html', ctx )



def editar_ficha_11(request, cod_censo):
	print 'PASOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
	ficha = FichaCenso.objects.get(pk=cod_censo)

	x = Prestamos.objects.filter(cod_censo=cod_censo)
	prestamo = PrestamosForm()

	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
		prestamos = []
		for prestamo in x:
			prestamo = PrestamosForm(instance=prestamo)
			prestamos.append(prestamo)
	else:
		print 'HOLA COMO ESTASAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
		form1 = FichaCensoForm(request.POST, instance=ficha)
		
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.prestamos_otros = None if request.POST.get('prestamos_otros') == '' else request.POST.get('prestamos_otros')
				ficha.tipo_institucion_prestamos = None if request.POST.get('tipo_institucion_prestamos') == '' else request.POST.get('tipo_institucion_prestamos')
				ficha.cod_vista = 13
				ficha.save()

				institucion = request.POST.getlist('institucion[]')
				tipo_prestamos = request.POST.getlist('tipo_prestamos[]')
				moneda = request.POST.getlist('moneda[]')
				tasa = request.POST.getlist('tasa[]')
				monto_original = request.POST.getlist('monto_original[]')
				plazo_meses = request.POST.getlist('plazo_meses[]')

				prestamo = Prestamos.objects.filter(cod_censo=cod_censo).delete()
				counter = 0
				for x in institucion:
					prestamo = Prestamos()
					prestamo.cod_censo = FichaCenso.objects.get(pk=cod_censo)
					prestamo.institucion = None if institucion[counter] == '' else institucion[counter]
					prestamo.tipo_prestamos = None if tipo_prestamos[counter] == '' else tipo_prestamos[counter]
					prestamo.moneda = None if moneda[counter] == '' else moneda[counter]
					prestamo.tasa = None if tasa[counter] == '' else tasa[counter]
					prestamo.monto_original = None if monto_original[counter] == '' else monto_original[counter]
					prestamo.plazo_meses = None if plazo_meses[counter] == '' else plazo_meses[counter]

					prestamo.save()
					counter += 1

				return redirect(reverse('editar_ficha_12', kwargs={'cod_censo': ficha.cod_censo}))				
		except Exception as e:
			raise e

	ctx = {
	'form1': form1,
	'ficha': ficha,
	'prestamos': prestamos,
	'prestamo': prestamo,

	}

	return render(request, 'editar/editar_ficha_11.html', ctx )



def editar_ficha_12(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.destino_pendiente_pago = None if request.POST.get('destino_pendiente_pago') == '' else request.POST.get('destino_pendiente_pago')
				ficha.otros_destino = None if request.POST.get('otros_destino') == '' else request.POST.get('otros_destino')
				ficha.cuenta_ahorro_otro = None if request.POST.get('cuenta_ahorro_otro') == '' else request.POST.get('cuenta_ahorro_otro')
				ficha.nombre_institucion_ahorro = None if request.POST.get('nombre_institucion_ahorro') == '' else request.POST.get('nombre_institucion_ahorro')
				ficha.tipo_cuenta_ahorro = None if request.POST.get('tipo_cuenta_ahorro') == '' else request.POST.get('tipo_cuenta_ahorro')
				ficha.otros_tipo_cuenta = None if request.POST.get('otros_tipo_cuenta') == '' else request.POST.get('otros_tipo_cuenta')
				ficha.tarjeta_credito = None if request.POST.get('tarjeta_credito') == '' else request.POST.get('tarjeta_credito')
				ficha.cantidad_tarjetas = None if request.POST.get('cantidad_tarjetas') == '' else request.POST.get('cantidad_tarjetas')
				ficha.nombre_institucion_tarjeta = None if request.POST.get('nombre_institucion_tarjeta') == '' else request.POST.get('nombre_institucion_tarjeta')
				ficha.tipo_tarjeta = None if request.POST.get('tipo_tarjeta') == '' else request.POST.get('tipo_tarjeta')
				ficha.cod_vista = 14				
				
	
				ficha.save()
				return redirect(reverse('editar_ficha_13', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_12.html', ctx )	



def editar_ficha_13(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.limite_tarjeta = None if request.POST.get('limite_tarjeta') == '' else request.POST.get('limite_tarjeta')
				ficha.tipo_compra_casa = None if request.POST.get('tipo_compra_casa') == '' else request.POST.get('tipo_compra_casa')
				ficha.cuota_casa_mensual = None if request.POST.get('cuota_casa_mensual') == '' else request.POST.get('cuota_casa_mensual')
				ficha.nombre_institucion_casa = None if request.POST.get('nombre_institucion_casa') == '' else request.POST.get('nombre_institucion_casa')
				ficha.sistema_cable = None if request.POST.get('sistema_cable') == '' else request.POST.get('sistema_cable')
				ficha.internet = None if request.POST.get('internet') == '' else request.POST.get('internet')
				ficha.cod_vista = 15		
	
				ficha.save()
				return redirect(reverse('editar_ficha_14', kwargs={'cod_censo': ficha.cod_censo}))
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_13.html', ctx )	




def editar_ficha_14(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.remesas_extrajero = None if request.POST.get('remesas_extrajero') == '' else request.POST.get('remesas_extrajero')
				ficha.pais_remesas = None if request.POST.get('pais_remesas') == '' else request.POST.get('pais_remesas')
				ficha.ciudad_remesas = None if request.POST.get('ciudad_remesas') == '' else request.POST.get('ciudad_remesas')	
				ficha.quien_envia = None if request.POST.get('quien_envia') == '' else request.POST.get('quien_envia')	
				ficha.uso_remesas = None if request.POST.get('uso_remesas') == '' else request.POST.get('uso_remesas')	
				ficha.empresa_remesas = None if request.POST.get('empresa_remesas') == '' else request.POST.get('empresa_remesas')	
				ficha.cada_cuanto_recibe = None if request.POST.get('cada_cuanto_recibe') == '' else request.POST.get('cada_cuanto_recibe')	
				ficha.promedio_remesas = None if request.POST.get('promedio_remesas') == '' else request.POST.get('promedio_remesas')	
				ficha.cod_vista = 16	
	
				ficha.save()
				return redirect(reverse('editar_ficha_15', kwargs={'cod_censo': ficha.cod_censo}))				
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_14.html', ctx )		
		



def editar_ficha_15(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)
	else:
		form1 = FichaCensoForm(request.POST, instance=ficha)
		try:
			with transaction.atomic():
				ficha = FichaCenso.objects.get(cod_censo=cod_censo)
				ficha.fecha_censo = None if request.POST.get('fecha_censo') == '' else request.POST.get('fecha_censo')
				ficha.cod_usuario = None if request.POST.get('cod_usuario') == '' else request.POST.get('cod_usuario')
				ficha.departamento_encuesta = Departamentos.objects.get(pk=request.POST.get('departamento_encuesta')) #el atributo 'name' del elemento <select>
				ficha.municipio_encuesta = Municipios.objects.get(pk=request.POST.get('cod_municipio')) #el atributo 'name' del elemento <select>
				ficha.filial_encuesta = Filiales.objects.get(pk=request.POST.get('filial_encuesta'))
				ficha.cod_estado = Estados.objects.get(pk=1)
				ficha.cod_vista = 17				
	
	
				ficha.save()
				return redirect(reverse('menu_principal', kwargs={}))				
			
		except Exception as e:
			mensaje = 'error'

	ctx = {
	'form1': form1,
	'ficha': ficha

	}			
		
	return render(request, 'editar/editar_ficha_15.html', ctx )		



# *****************************************************AJAX*******************************************************************************
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


def atras_1(request, cod_censo):
	ficha = FichaCenso.objects.get(pk=cod_censo)
	
	if request.method == 'GET':
		form1 = FichaCensoForm(instance=ficha)

	# else:
	# 	form1 = FichaCensoForm(request.POST, instance=ficha)
	# 	try:
	# 		with transaction.atomic():
	# 			ficha = FichaCenso.objects.get(cod_censo=cod_censo)			
			
	# 	except Exception as e:
	# 		raise e
		
	return render(request, 'editar/editar_ficha_1.html', {'form1': form1})	

