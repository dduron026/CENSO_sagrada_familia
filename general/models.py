from __future__ import unicode_literals

from django.db import models


class Departamentos(models.Model):
	cod_departamenton = models.AutoField(db_column='CodDepartamenton', primary_key=True)  # Field name made lowercase.
	desc_departamento = models.CharField(db_column='DescDepartamento', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[Departamentos'

	def __unicode__(self):
		return self.desc_departamento        



class Encuestadores(models.Model):
	cod_encuestador = models.AutoField(db_column='CodEncuestador', primary_key=True)  # Field name made lowercase.
	nombre_encuestador = models.CharField(db_column='NombreEncuestador', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[Encuestadores'


class Estados(models.Model):
	cod_estado = models.AutoField(db_column='CodEstado', primary_key=True)  # Field name made lowercase.
	desc_estado = models.CharField(db_column='DescEstado', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[Estados'


class FichaCenso(models.Model):
	cod_censo = models.AutoField(db_column='CodCenso', primary_key=True)  # Field name made lowercase.
	cod_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
	cod_encuestador = models.ForeignKey(Encuestadores, models.DO_NOTHING, db_column='CodEncuestador', blank=True, null=True)  # Field name made lowercase.
	#primera vista
	identidad = models.CharField(db_column='Identidad', max_length=15, blank=True, null=True)  # Field name made lowercase.
	nombres = models.CharField(db_column='Nombres', max_length=100, blank=True, null=True)  # Field name made lowercase.
	primer_apellido = models.CharField(db_column='PrimerApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
	segundo_apellido = models.CharField(db_column='SegundoApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
	fecha_nacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
	cod_departament_nacimiento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDepartamentNacimiento',related_name='CodDepartamentNacimiento_Deptos', blank=True, null=True)  # Field name made lowercase.
	cod_municipio_nacimiento = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='CodMunicipioNacimiento', related_name='CodMunicipioNacimiento_MunNa', blank=True, null=True)  # Field name made lowercase.
	edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
	numero_afiliado = models.CharField(db_column='NumeroAfiliado', max_length=15, blank=True, null=True)  # Field name made lowercase.
	genero = models.CharField(db_column='Genero', max_length=1, blank=True, null=True)  # Field name made lowercase.
	estado_civil = models.CharField(db_column='EstadoCivil', max_length=1, blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 2
	nivel_educativo = models.CharField(db_column='NivelEducativo', max_length=1, blank=True, null=True)  # Field name made lowercase.
	cod_profesion_oficio = models.ForeignKey('ProfesionOficio', models.DO_NOTHING, db_column='CodProfesionOficio', blank=True, null=True)  # Field name made lowercase.
	cod_departament_domicilio = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDepartamentDomicilio', related_name='CodDepartamentDomicilio_Deptos', blank=True, null=True)  # Field name made lowercase.
	cod_municipio_domicilio = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='CodMunicipioDomicilio', related_name='CodMunicipioDomicilio_Muni', blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 3 
	barrio_o_colonia_domicilio = models.CharField(db_column='BarrioColoniaDomicilio', max_length=100, blank=True, null=True)  # Field name made lowercase.
	calle_domicilio = models.CharField(db_column='CalleDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.    
	avenida_domicilio = models.CharField(db_column='AvenidaDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.    
	bloque_domicilio = models.CharField(db_column='BloqueDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	no_casa_domicilio = models.CharField(db_column='NoCasaDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	color_domicilio = models.CharField(db_column='ColorDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	punto_referencia_domicilio = models.CharField(db_column='PuntoReferenciaDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	telefono_fijo_domicilio = models.CharField(db_column='TelefonoFijoDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	telefono_otro_domicilio = models.CharField(db_column='TelefonoOtroDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	celular_domicilio = models.CharField(db_column='CelularDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	correo_electronico_domicilio = models.CharField(db_column='CorreoElectronicoDomicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 4
	conyuge = models.NullBooleanField(db_column='Conyuge')  # Field name made lowercase.   
	identidad_conyuge = models.CharField(db_column='IdentidadConyuge', max_length=50, blank=True, null=True)  # Field name made lowercase.
	nombres_conyuge = models.CharField(db_column='NombresConyuge', max_length=50, blank=True, null=True)  # Field name made lowercase.
	primer_apellido_conyuge = models.CharField(db_column='PrimerApellidoConyuge', max_length=50, blank=True, null=True)  # Field name made lowercase.
	segundo_apellido_conyuge = models.CharField(db_column='SegundoApellidoConyuge', max_length=50, blank=True, null=True)  # Field name made lowercase.
	apellido_de_casada = models.CharField(db_column='ApellidoCasada', max_length=50, blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 5
	trabaja_actualmente = models.NullBooleanField(db_column='TrabajaActualmente')  # Field name made lowercase.
	lugar_de_trabajo = models.CharField(db_column='LugarTrabajo', max_length=1, blank=True, null=True)  # Field name made lowercase.
	tipo_contratacion = models.CharField(db_column='TipoContratacion', max_length=1, blank=True, null=True)  # Field name made lowercase.
	antiguedad_meses = models.IntegerField(db_column='AntiguedadMeses', blank=True, null=True)  # Field name made lowercase.
	nombre_empresa = models.CharField(db_column='NombreEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.   
	departamento_o_seccion = models.CharField(db_column='DeptoSeccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
	cargo = models.CharField(db_column='Cargo', max_length=50, blank=True, null=True)  # Field name made lowercase.
	cod_departamento_empresa = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDepartamentEmpresa', related_name='CodDepartamentEmpresa_Deptos', blank=True, null=True)  # Field name made lowercase.
	cod_municipio_empresa = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='CodMunicipioEmpresa', related_name='CodMunicipioEmpresa_Muni', blank=True, null=True)  # Field name made lowercase.
	barrio_o_colonia_empresa = models.CharField(db_column='BarrioColoniaDEmpresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
	calle_empresa = models.CharField(db_column='CalleEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.   
	
	# VISTA 6
	avenida_empresa = models.CharField(db_column='AvenidaEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	bloque_empresa = models.CharField(db_column='BloqueEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	no_casa_empresa = models.CharField(db_column='NoCasaEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	color_empresa = models.CharField(db_column='ColorEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	etapa_empresa = models.CharField(db_column='EtapaEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	punto_referencia_empresa = models.CharField(db_column='PuntoReferenciaEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	telefono_fijo_empresa = models.CharField(db_column='TelefonoFijoEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	telefono_otro_empresa = models.CharField(db_column='TelefonoOtroEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	celular_empresa = models.CharField(db_column='CelularEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	correo_electronico_empresa = models.CharField(db_column='CorreoElectronicoEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 7
	negocio_propio = models.NullBooleanField(db_column='NegocioPropio')  # Field name made lowercase.
	negocio_especificar = models.CharField(db_column='NegocioEspecificar', max_length=50, blank=True, null=True)  # Field name made lowercase.
	num_empleados = models.IntegerField(db_column='NumEmpleados', blank=True, null=True)  # Field name made lowercase.
	antiguedad_negocio_meses = models.IntegerField(db_column='AntiguedadNegocioMeses', blank=True, null=True)  # Field name made lowercase.
	rubro_negocio = models.CharField(db_column='RubroNegocio', max_length=50, blank=True, null=True)  # Field name made lowercase.
	otros_ingresos = models.NullBooleanField(db_column='OtrosIngresos')  # Field name made lowercase.
	cantidad_promedio = models.DecimalField(db_column='CantidadPromedio', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
	nivel_ingreso = models.CharField(db_column='NivelIngreso', max_length=1, blank=True, null=True)  # Field name made lowercase.
	trabaja_conyuge = models.NullBooleanField(db_column='TrabajaConyuge')  # Field name made lowercase.
	nivel_ingreso_conyuge = models.CharField(db_column='NivelIngresoConyuge', max_length=1, blank=True, null=True)  # Field name made lowercase.    
	
	# VISTA 8
	hijos = models.NullBooleanField(db_column='Hijos')  # Field name made lowercase.
	cantidad_hijos = models.IntegerField(db_column='CantidadHijos', blank=True, null=True) 

	# VISTA 9......
	hijos_afiliados = models.NullBooleanField(db_column='HijosAfiliados')  # Field name made lowercase.
	papel_casa = models.CharField(db_column='PapelCasa', max_length=1, blank=True, null=True)  # Field name made lowercase.
	vehiculo = models.NullBooleanField(db_column='Vehiculo')  # Field name made lowercase.
	cantidad_vehiculos = models.IntegerField(db_column='CantidadVehiculos', blank=True, null=True)  # Field name made lowercase.
	tipo_casa = models.CharField(db_column='TipoCasa', max_length=1, blank=True, null=True)  # Field name made lowercase.
	numero_habitaciones = models.IntegerField(db_column='NumeroHabitaciones', blank=True, null=True)  # Field name made lowercase.
	numero_televisores = models.IntegerField(db_column='NumeroTelevisores', blank=True, null=True)  # Field name made lowercase.
	cantidad_personas = models.IntegerField(db_column='CantidadPersonas', blank=True, null=True)  # Field name made lowercase.
	numero_ninos = models.IntegerField(db_column='NumeroNinos', blank=True, null=True)  # Field name made lowercase.
	numero_adolescentes = models.IntegerField(db_column='NumeroAdolescentes', blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 10 
	mayores_edad = models.IntegerField(db_column='MayoresEdad', blank=True, null=True)  # Field name made lowercase.
	mayores_a_60 = models.IntegerField(db_column='Mayoresa60', blank=True, null=True)  # Field name made lowercase.
	anos_afiliacion = models.IntegerField(db_column='AnosAfiliacion', blank=True, null=True)  # Field name made lowercase.
	tipo_afiliado = models.CharField(db_column='TipoAfiliado', max_length=1, blank=True, null=True)  # Field name made lowercase.
	cod_filial_afiliacion = models.ForeignKey('Filiales', models.DO_NOTHING, db_column='CodFilialAfiliacion',  related_name='CodFilialAfiliacion_Filiales', blank=True, null=True)  # Field name made lowercase.
	cod_filial_visita = models.ForeignKey('Filiales', models.DO_NOTHING, db_column='CodFilialVisita',  related_name='CodFilialVisita_Filiales', blank=True, null=True)  # Field name made lowercase.
	cursos_capacitaciones = models.NullBooleanField(db_column='CursosCapacitaciones')  # Field name made lowercase.
	asambleas_sectoriales = models.NullBooleanField(db_column='AsambleasSectoriales')  # Field name made lowercase.
	
	# VISTA 11
	prestamos_otros = models.NullBooleanField(db_column='PrestamosOtros')  # Field name made lowercase.
	tipo_institucion_prestamos = models.CharField(db_column='TipoInstitucionPrestamos', max_length=1, blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 12
	destino_pendiente_pago = models.CharField(db_column='DestinoPendientePago', max_length=1, blank=True, null=True)  # Field name made lowercase.
	otros_destino = models.CharField(db_column='OtrosDesinto', max_length=100, blank=True, null=True)  # Field name made lowercase.
	cuenta_ahorro_otro = models.NullBooleanField(db_column='CuentaAhorroOtro')  # Field name made lowercase.
	nombre_institucion_ahorro = models.CharField(db_column='NombreInstitucionAhorro', max_length=100, blank=True, null=True)  # Field name made lowercase.
	tipo_cuenta_ahorro = models.CharField(db_column='TipoCuentaAhorro', max_length=1, blank=True, null=True)  # Field name made lowercase.
	otros_tipo_cuenta = models.CharField(db_column='OtrosTipoCuenta', max_length=100, blank=True, null=True)  # Field name made lowercase.
	tarjeta_credito = models.NullBooleanField(db_column='TarjetaCredito')  # Field name made lowercase.
	cantidad_tarjetas = models.IntegerField(db_column='CantidadTarjetas', blank=True, null=True)  # Field name made lowercase.
	nombre_institucion_tarjeta = models.CharField(db_column='NombreInstitucionTarjeta', max_length=100, blank=True, null=True)  # Field name made lowercase.
	tipo_tarjeta = models.CharField(db_column='TipoTarjeta', max_length=1, blank=True, null=True)  # Field name made lowercase.
	

	# VISTA 13
	limite_tarjeta = models.CharField(db_column='LimiteTarjeta', max_length=1, blank=True, null=True)  # Field name made lowercase.
	tipo_compra_casa = models.CharField(db_column='TipoCompraCasa', max_length=1, blank=True, null=True)  # Field name made lowercase.
	cuota_casa_mensual = models.DecimalField(db_column='CuotaCasaMensual', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
	nombre_institucion_casa = models.CharField(db_column='NombreInsitucionCasa', max_length=100, blank=True, null=True)  # Field name made lowercase.
	sistema_cable = models.NullBooleanField(db_column='SistemaCable')  # Field name made lowercase.
	internet = models.NullBooleanField(db_column='Internet')  # Field name made lowercase.
	
	# VISTA 14
	remesas_extrajero = models.NullBooleanField(db_column='RemesasExtrajero')  # Field name made lowercase.
	pais_remesas = models.CharField(db_column='PaisRemesas', max_length=100, blank=True, null=True)  # Field name made lowercase.
	ciudad_remesas = models.CharField(db_column='CiudadRemesas', max_length=100, blank=True, null=True)  # Field name made lowercase.
	quien_envia = models.CharField(db_column='QuienEnvia', max_length=100, blank=True, null=True)  # Field name made lowercase.
	uso_remesas = models.CharField(db_column='UsoRemesas', max_length=1, blank=True, null=True)  # Field name made lowercase.
	empresa_remesas = models.CharField(db_column='EmpresaRemesas', max_length=1, blank=True, null=True)  # Field name made lowercase.
	cada_cuanto_recibe = models.CharField(db_column='CadaCuantoRecibe', max_length=1, blank=True, null=True)  # Field name made lowercase.
	promedio_remesas = models.CharField(db_column='PromedioRemesas', max_length=1, blank=True, null=True)  # Field name made lowercase.
	
	# VISTA 15
	fecha_censo = models.DateTimeField(db_column='FechaCenso', blank=True, null=True)  # Field name made lowercase.
	cod_usuario = models.IntegerField(db_column='CodUsuario', blank=True, null=True)  # Field name made lowercase.
	departamento_encuesta = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='DepartamentEncuesta', blank=True, null=True)  # Field name made lowercase.
	municipio_encuesta = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='MunicipioEncuesta', blank=True, null=True)  # Field name made lowercase.
	filial_encuesta = models.ForeignKey('Filiales', models.DO_NOTHING, db_column='FilialEncuesta', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[FichaCenso'


class Filiales(models.Model):
	cod_filial = models.AutoField(db_column='CodFilial', primary_key=True)  # Field name made lowercase.
	nombre_filial = models.CharField(db_column='NombreFilial', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[Filiales'

	def __unicode__(self):
		return self.nombre_filial		


class Hijos(models.Model):
	cod_hijo = models.AutoField(db_column='CodHijo', primary_key=True)  # Field name made lowercase.
	cod_censo = models.ForeignKey(FichaCenso, models.DO_NOTHING, db_column='CodCenso',  related_name='CodCenso_Hijos', blank=True, null=True)  # Field name made lowercase.
	num_hijo = models.IntegerField(db_column='NumHijo', blank=True, null=True)  # Field name made lowercase.
	nombre_hijo = models.CharField(db_column='NombreHijo', max_length=150, blank=True, null=True)  # Field name made lowercase.
	edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
	estudia_trabaja = models.CharField(db_column='EstudiaTrabaja', max_length=1, blank=True, null=True)  # Field name made lowercase.
	nivel_estudio = models.CharField(db_column='NivelEstudio', max_length=1, blank=True, null=True)  # Field name made lowercase.
	institucion_estudio = models.CharField(db_column='InstitucionEstudio', max_length=1, blank=True, null=True)  # Field name made lowercase.
	institucion_trabajo = models.CharField(db_column='InstitucionTrabajo', max_length=1, blank=True, null=True)  # Field name made lowercase.
	sueldo = models.DecimalField(db_column='Sueldo', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[Hijos'


class HistEstados(models.Model):
	cod_cambio = models.AutoField(db_column='CodCambio', primary_key=True)  # Field name made lowercase.
	cod_censo = models.ForeignKey(FichaCenso, models.DO_NOTHING, db_column='CodCenso', blank=True, null=True)  # Field name made lowercase.
	cod_estado = models.IntegerField(db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
	cod_usuario = models.IntegerField(db_column='CodUsuario', blank=True, null=True)  # Field name made lowercase.
	fecha_hora = models.DateTimeField(db_column='FechaHora', blank=True, null=True)  # Field name made lowercase.
	observaciones = models.CharField(db_column='Observaciones', max_length=400, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[HistEstados'


class Municipios(models.Model):
	cod_municipio = models.AutoField(db_column='CodMunicipio', primary_key=True)  # Field name made lowercase.
	cod_departamento = models.ForeignKey(Departamentos, db_column='CodDepartamento', blank=True, null=True)  # Field name made lowercase.
	desc_municipio = models.CharField(db_column='DescMunicipio', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[Municipios'

	def __unicode__(self):
		return self.desc_municipio	

class Prestamos(models.Model):
	cod_prestamos = models.AutoField(db_column='CodPrestamos', primary_key=True)  # Field name made lowercase.
	cod_censo = models.ForeignKey(FichaCenso, models.DO_NOTHING, db_column='CodCenso', blank=True, null=True)  # Field name made lowercase.
	institucion = models.CharField(db_column='Institucion', max_length=100, blank=True, null=True)  # Field name made lowercase.
	tipo_prestamos = models.IntegerField(db_column='TipoPrestamos', blank=True, null=True)  # Field name made lowercase.
	moneda = models.CharField(db_column='Moneda', max_length=1, blank=True, null=True)  # Field name made lowercase.
	tasa = models.DecimalField(db_column='Tasa', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
	monto_original = models.DecimalField(db_column='MontoOriginal', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
	plazo_meses = models.IntegerField(db_column='PlazoMeses', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[Prestamos'


class ProfesionOficio(models.Model):
	cod_profesion_oficio = models.AutoField(db_column='CodProfesionOficio', primary_key=True)  # Field name made lowercase.
	desc_profesion = models.CharField(db_column='DescProfesion', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Censo].[ProfesionOficio'

	def __unicode__(self):
		return self.desc_profesion
