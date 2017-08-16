# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from general.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group

GENERO = (
	('M', 'Masculino'),
	('F', 'Femenino'),
	
)

ESTADO_CIVIL = (
	
	('A', 'Soltero'),
	('B', 'Casado(a)'),
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

PAPEL_CASA = (
	
	('', '--------'),
	('A', 'Hija(o) '),
	('B', 'Madre/padre de familia'),
	('C', 'Abuela'),
	('D', 'Otro'),
	
)

SE_DEDICA = (
	('','---------'),	
	('A', 'Estudia'),
	('B', 'Trabaja'),
	('C', 'Ambos'),
)

NIVEL_ESTUDIO_HIJO = (
	('','---------'),
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

INSTITICION_ESTUDIA = (
	('','---------'),
	('A', 'Privada'),
	('B', 'Pública'),	
)

INSTITICION_TRABAJA = (
	('','---------'),
	('A', 'Privada'),
	('B', 'Pública'),	
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

HIJOS_AFILIADOS = (
	(True, 'Si'),
	(False, 'No'),
	)


POSEE_VEHICULO = (
	(True, 'Si'),
	(False, 'No'),
	)

CURSOS = (
	(True, 'Si'),
	(False, 'No'),
	)

ASAMBLEAS = (
	(True, 'Si'),
	(False, 'No'),
	)

PRESTAMOS_OTROS = (
	(True, 'Si'),
	(False, 'No'),
	)

CUENTA_AHORRO_OTRO = (
	(True, 'Si'),
	(False, 'No'),
	)

TARJETA_CREDITO = (
	(True, 'Si'),
	(False, 'No'),
	)


SISTEMA_CABLE = (
	(True, 'Si'),
	(False, 'No'),
	)


INTERNET = (
	(True, 'Si'),
	(False, 'No'),
	)


REMESAS = (
	(True, 'Si'),
	(False, 'No'),
	)


LUGAR_TRABAJO = (

	('', '---------'),
	('A', 'Gobierno Central'),
	('B', 'Institución Autónoma'),
	('C', 'Municipalidad'),
	('D', 'Empresa Privada'),
	)

TIPO_CONTRATO = (
	('','---------'),
	('A','Permanente'),
	('B','Temporal'),
	('C','Por horas'),
	)

TIPO_AFILIADO = (
	('','---------'),
	('A','Planilla'),
	('B','Ventanilla'),
	
	)

TIPO_CASA = (
	('','---------'),
	('A','Propia'),
	('B','Alquilada'),
	('C','Familiar'),
	)

INSTITUCION_OTROS_PRESTAMOS = (
	('','---------'),
	('A','Bancos'),
	('B','Cooperativas'),
	('C','Sistema de prevención'),
	('D','Financieras'),
	('E','OPDF'),
	('F','Prestamistas'),
	)


OTROS_PRESTAMOS_DESTINO = (
	('','---------'),
	('A','Compra de casa'),
	('B','Compra de Terreno'),
	('C','Compra de Vehículo'),
	('D','Viajes'),
	('E','Consumo'),
	('F','Salud'),
	('G','Consolidación de deudas tarjetas de crédito'),
	('H','Gastos educativos hijos '),
	)

TIPO_CUENTA_AHORRO = (
	('','---------'),
	('A','DPF'),
	('B','Cuenta Retirable'),
	('C','Fondo de pensiones'),
	('D','Cuenta de cheques'),
	('E','Cuenta de ahorro programado'),
	)

TIPO_TARJETA_CREDITO = (
	('','---------'),
	('A','Clásica'),
	('B','Oro'),
	('C','Platinum'),
	('D','Otra'),	
	)

LIMITE_TARJETA = (
	('','---------'),
	('A','Hasta $400.00'),
	('B','De $401 a $800'),
	('C','De $800 a $1200'),
	('D','De $1201 a $3,000'),	
	('E','$3,000 en adelante'),	
	)

TIPO_COMPRA_CASA = (
	('','---------'),
	('A','Propia'),
	('B','Alquilada'),
	('C','Familiar'),
	('D','Pagándola'),	
	)

USO_REMESAS = (
	('','---------'),
	('A','Gastos de casa'),
	('B','Educación de los hijos'),
	('C','Medicinas'),
	('D','Pago de deudas'),	
	('E','Otros'),	
	)


EMPRESA_REMESAS = (
	('','---------'),
	('A','Wester Unión'),
	('B','Money Gram'),
	('C','Tigo'),
	('D','Vigo'),	
	('E','Otras'),	
	)

PROMEDIO_REMESAS = (
	('','---------'),
	('A','Menos de $100'),
	('B','De $101 a $200'),
	('C','De $201 a $350'),
	('D','De $351 a $500'),	
	('E','De $501 en adelante'),	
	)


CADA_CUANTO_RECIBE = (
	('','---------'),
	('A','Semanal'),
	('B','Quincenal'),
	('C','Mensual'),
	('D','Cada dos meses'),	
	('E','Cada seis meses'),	
	('F','Una vez al año'),	
	)

MONEDA = (
	('','---------'),
	('A','Lempiras'),
	('B','Dólares'),

	)

TIPO_PRESTAMO = (
	('','---------'),
	('A','Préstamo Hipotecario'),
	('B','Préstamo de consumo'),
	('C','Tarjeta de crédito'),

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
	papel_casa = forms.ChoiceField(choices=PAPEL_CASA, label='Papel en la casa', required=False)
	tipo_casa = forms.ChoiceField(choices=TIPO_CASA, label='Tipo Casa', required=False)
	hijos_afiliados = forms.ChoiceField(widget=RadioSelect, choices=HIJOS_AFILIADOS, label='Están afiliados sus hijos?', required=False)
	vehiculo = forms.ChoiceField(widget=RadioSelect, choices=POSEE_VEHICULO, label='Posee vehículo?', required=False)
	cursos_capacitaciones = forms.ChoiceField(widget=RadioSelect, choices=CURSOS, label='Cursos y capacitaciones', required=False)
	asambleas_sectoriales = forms.ChoiceField(widget=RadioSelect, choices=ASAMBLEAS, label='Asambleas sectoriales', required=False)
	prestamos_otros = forms.ChoiceField(widget=RadioSelect, choices=PRESTAMOS_OTROS, label='Tiene Préstamo con otra institución', required=False)
	tipo_institucion_prestamos = forms.ChoiceField(choices=INSTITUCION_OTROS_PRESTAMOS, label='Con qué otra institución tiene Préstamo', required=False)
	destino_pendiente_pago = forms.ChoiceField(choices=OTROS_PRESTAMOS_DESTINO, label='Los Préstamos pendientes de pago fueron para', required=False)
	cuenta_ahorro_otro = forms.ChoiceField(widget=RadioSelect, choices=CUENTA_AHORRO_OTRO, label='Tiene cuenta de ahorro en otra institución', required=False)
	tipo_cuenta_ahorro = forms.ChoiceField(choices=TIPO_CUENTA_AHORRO, label='Qué tipo de cuenta de ahorro mantiene con esas instituciones', required=False)
	tarjeta_credito = forms.ChoiceField(widget=RadioSelect, choices=TARJETA_CREDITO, label='Tiene tarjeta de crédito', required=False)
	tipo_tarjeta = forms.ChoiceField(choices=TIPO_TARJETA_CREDITO, label='Tipo de tarjeta', required=False)
	limite_tarjeta = forms.ChoiceField(choices=LIMITE_TARJETA, label='Limite de tarjeta', required=False)
	tipo_compra_casa = forms.ChoiceField(choices=TIPO_COMPRA_CASA, label='La casa donde usted vive es:', required=False)
	sistema_cable = forms.ChoiceField(widget=RadioSelect, choices=SISTEMA_CABLE, label='Tiene sistema de cable en hogar', required=False)
	internet = forms.ChoiceField(widget=RadioSelect, choices=INTERNET, label='Tiene internet en su hogar', required=False)
	remesas_extrajero = forms.ChoiceField(widget=RadioSelect, choices=REMESAS, label='Recibe remesas del extranjero', required=False)
	uso_remesas = forms.ChoiceField(choices=USO_REMESAS, label='Para qué usa el dinero que recibe del extranjero', required=False)
	empresa_remesas = forms.ChoiceField(choices=EMPRESA_REMESAS, label='Por qué empresa recibe o envía sus remesas', required=False)
	cada_cuanto_recibe = forms.ChoiceField(choices=CADA_CUANTO_RECIBE, label='Cada cuánto le envía remesas', required=False)
	promedio_remesas = forms.ChoiceField(choices=PROMEDIO_REMESAS, label='Valor promedio de remesas que recibe', required=False)
	tipo_afiliado = forms.ChoiceField(choices=TIPO_AFILIADO, label='Tipo de Afiliado', required=False)
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
		'num_empleados':('Número de empleados'), 'cantidad_vehiculos': ('Cantidad de vehículos'),
		'cantidad_personas': ('Cantidad de personas que viven en la casa'),
		'numero_ninos': ('Cantidad de Niños'), 'numero_adolescentes': ('Cantidad de adololescentes'),
		'mayores_edad': ('Cantidad de mayores de edad'), 'mayores_a_60': ('Cantidad de mayores a 60'),
		'anos_afiliacion': ('Cuantos años tiene de ser afiliado'), 'nombre_institucion_ahorro': ('Nombre institución de ahorro'),
		'otros_tipo_cuenta':('Otras (especifique)'),'nombre_institucion_tarjeta':('Con que institución(es) tiene tarjeta de crédito'),
		'nombre_institucion_casa': ('Banco'),'pais_remesas': ('De qué país'),'ciudad_remesas':('Ciudad'),
		'quien_envia': ('Quien le envía'), 'cod_usuario': ('Código del Usuario'),
		'cod_filial_afiliacion':('En qué filial se afilió'),
		'cod_filial_visita':('Qué filial visita con más frecuencia')
		

		 }



class HijosForm(ModelForm):

	estudia_trabaja = forms.ChoiceField(choices=SE_DEDICA, label='A qué se dedica', required=False)
	nivel_estudio = forms.ChoiceField(choices=NIVEL_ESTUDIO_HIJO, label='Nivel de estudio', required=False)
	institucion_estudio = forms.ChoiceField(choices=INSTITICION_ESTUDIA, label='Institución donde estudia es', required=False)
	institucion_trabajo = forms.ChoiceField(choices=INSTITICION_TRABAJA, label='Institución donde trabaja es', required=False)


	class Meta:
		model = Hijos
		fields = "__all__"
		exclude = []
		labels = {'num_hijo':('Hijo Nro.'),
				 'nombre_hijo':('Nombre del hijo'),
				 'institucion':('Institución'),
				 'tipo_prestamos':('Tipo de préstamo'),
				 'plazo_meses':('Plazo en meses'),
				 }

class PrestamosForm(ModelForm):

	moneda = forms.ChoiceField(choices=MONEDA, label='Moneda', required=False)
	tipo_prestamos = forms.ChoiceField(choices=TIPO_PRESTAMO, label='Tipo de préstamo', required=False)


	class Meta:
		model = Prestamos
		fields = "__all__"
		exclude = []
		labels = {
				 'institucion':('Institución'),			
				 'plazo_meses':('Plazo en meses'),
				 }

class ProfesionOficioForm(ModelForm):

	class Meta:
		model = ProfesionOficio
		fields = "__all__"
		exclude = []
		labels = {
				'desc_profesion':('Profesión u oficio'),
				}


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = "__all__"
		exclude = []
		labels = {}		


class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = "__all__"
		exclude = []
		labels = {}		







	
		

