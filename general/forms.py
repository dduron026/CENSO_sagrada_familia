# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from general.models import *
from django.utils.translation import ugettext_lazy as _

GENERO = (
	('M', 'Masculino'),
	('F', 'Femenino'),
	
)

ESTADO_CIVIL = (
	
	('A', 'Soltero'),
	('B', 'Casado'),
	('C', 'Union Libre'),
	('D', 'Viudo'),
	('E', 'Divorciado'),

)

# varchar(1)
NIVEL_EDUCATIVO = (
	('A', 'Ninguno'),
	('B', 'Primaria Incompleta'),
	('C', 'Primaria Completa'),
	('D', 'Secundaria'),
	('E', 'Técnico Medio '),
	('F', 'Técnico Superior'),
	('G', 'Universidad'),
	('H', 'Posgrado'),
	('I', 'NS/NR'),
)

NIVEL_INGRESO = (
	
	('', '--------'),
	('A', 'Hasta L. 7,000'),
	('B', 'De L. 7,001 a 10,000'),
	('C', 'De L. 10,001 a 20,000'),
	('D', 'De L. 20,000.01 en adelante'),
	
)

NIVEL_INGRESO_CONYUGUE = (
	
	('', '--------'),
	('A', 'Hasta L. 7,000'),
	('B', 'De L. 7,001 a 10,000'),
	('C', 'De L. 10,001 a 20,000'),
	('D', 'De L. 20,000.01 en adelante'),
	
)

# bit
CONYUGUE = (
	(True, 'Si'),
	(False, 'No'),
	)

TRABAJA = (
	(True, 'Si'),
	(False, 'No'),
	)

TRABAJA_CONYUGUE = (
	(True, 'Si'),
	(False, 'No'),
	)


NEGOCIO_PROPIO = (
	(True, 'Si'),
	(False, 'No'),
	)

OTROS_INGRESOS = (
	(True, 'Si'),
	(False, 'No'),
	)

TIENE_HIJOS = (
	(True, 'Si'),
	(False, 'No'),
	)

LUGAR_TRABAJO = (

	('', '------'),
	('A', 'Gobierno Central'),
	('B', 'Institución Autónoma'),
	('C', 'Municipalidad'),
	('D', 'Empresa Privada'),
	)

TIPO_CONTRATO = (
	('','------'),
	('A','Permanente'),
	('A','Temporal'),
	('A','Por horas'),
	)

class FichaCensoForm(ModelForm):

	genero = forms.ChoiceField(widget=RadioSelect, choices=GENERO, required=False)
	estado_civil = forms.ChoiceField(widget=RadioSelect, choices=ESTADO_CIVIL, required=False)
	nivel_educativo = forms.ChoiceField(widget=RadioSelect, choices=NIVEL_EDUCATIVO, required=False)
	conyuge = forms.ChoiceField(label='Cónyugue', widget=RadioSelect, choices=CONYUGUE, required=False)
	trabaja_actualmente = forms.ChoiceField(widget=RadioSelect, choices=TRABAJA, required=False)
	lugar_de_trabajo = forms.ChoiceField(choices=LUGAR_TRABAJO, required=False)
	tipo_contratacion = forms.ChoiceField(label='Tipo contrato', choices=TIPO_CONTRATO, required=False)
	negocio_propio = forms.ChoiceField(widget=RadioSelect, choices=NEGOCIO_PROPIO, required=False)
	otros_ingresos = forms.ChoiceField(widget=RadioSelect, choices=OTROS_INGRESOS, required=False)
	trabaja_conyuge = forms.ChoiceField(widget=RadioSelect, choices=TRABAJA_CONYUGUE, required=False)
	nivel_ingreso = forms.ChoiceField(choices=NIVEL_INGRESO, label='Nivel de ingreso', required=False)
	nivel_ingreso_conyuge = forms.ChoiceField(choices=NIVEL_INGRESO_CONYUGUE, label='Nivel de ingreso cónyugue', required=False)
	hijos = forms.ChoiceField(widget=RadioSelect, choices=TIENE_HIJOS, label='Tiene hijos', required=False)
	
	class Meta:
		model = FichaCenso
		fields = "__all__"
		exclude = []
		labels = {'cod_departament_nacimiento': ('Departamento nacimiento'),'cod_municipio_nacimiento': ('Municipio nacimiento'),
		'cod_profesion_oficio': ('Profesión u oficio'), 'cod_departament_domicilio': ('Departamento Domicilio'),
		'no_casa_domicilio': ('Número de casa'),'identidad_conyuge': ('Identidad cónyuge'),
		'nombres_conyugue': ('Nombres cónyugue'),'primer_apellido_conyuge': ('Primer apellido cónyuge'),
		'cod_departamento_empresa':('Departamento'), 'cod_municipio_empresa': ('Municipio'),
		'barrio_o_colonia_empresa':('Barrio o colonia'),'calle_empresa':('Calle'),
		'no_casa_empresa':('Número de casa empresa'),'telefono_fijo_empresa': ('Teléfono fijo empresa'),
		'telefono_otro_empresa': ('Otro teléfono'),'correo_electronico_empresa': ('Correo electrónico empresa'),
		'negocio_especificar':('Tipo de Negocio'), 'antiguedad_negocio_meses':('Antigüedad negocio en meses'),
		'num_empleados':('Número de empleados'),}



class IngresarHijosForm(ModelForm):

	class Meta:
		model = Hijos
		fields = "__all__"
		exclude = []
		labels = {}
	
		

