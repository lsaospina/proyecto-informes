from django.db import models

class TiposIdentificacion(models.Model):
    tipo_ident_id = models.AutoField(primary_key=True)
    tipo_ident_nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_identificacion'
        
class TiposBeneficiarios(models.Model):
    tipo_benef_id = models.AutoField(primary_key=True)
    tipo_benef_nombre = models.CharField(max_length=80, blank=True, null=True)
    montoactivos = models.BigIntegerField(db_column='MontoActivos', blank=True, null=True)  # Field name made lowercase.
    idtipoproductor = models.IntegerField(db_column='IdTipoProductor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipos_beneficiarios'
        
class Beneficiarios(models.Model):
    benef_id = models.AutoField(primary_key=True)
    benef_nombre = models.CharField(max_length=100, blank=True, null=True)
    benef_primer_nombre = models.CharField(max_length=80, blank=True, null=True)
    benef_segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    benef_primer_apellido = models.CharField(max_length=50, blank=True, null=True)
    benef_segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    benef_direccion = models.CharField(max_length=80, blank=True, null=True)
    benef_telefono = models.CharField(max_length=40, blank=True, null=True)
    benef_celular = models.CharField(max_length=50, blank=True, null=True)
    benef_celular2 = models.CharField(max_length=50, blank=True, null=True)
    benef_celular3 = models.CharField(max_length=50, blank=True, null=True)
    benef_email = models.CharField(max_length=90, blank=True, null=True)
    benef_email2 = models.CharField(max_length=90, blank=True, null=True)
    benef_email3 = models.CharField(max_length=90, blank=True, null=True)
    benef_web = models.CharField(max_length=100, blank=True, null=True)
    ciudad_id = models.IntegerField(blank=True, null=True)
    depto_id = models.IntegerField(blank=True, null=True)
    tipo_ident = models.ForeignKey('TiposIdentificacion', models.DO_NOTHING, blank=True, null=True)
    benef_ident_no = models.DecimalField(max_digits=28, decimal_places=0, blank=True, null=True)
    div = models.IntegerField(blank=True, null=True)
    tipo_benef = models.ForeignKey('TiposBeneficiarios', models.DO_NOTHING, blank=True, null=True)
    usuario_id = models.IntegerField(blank=True, null=True)
    benef_fecha = models.DateTimeField(blank=True, null=True)
    benef_observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_persona = models.IntegerField(blank=True, null=True)
    idclientecrm = models.BigIntegerField(blank=True, null=True)
    int_benef_id = models.IntegerField(blank=True, null=True)
    act_agro = models.IntegerField(blank=True, null=True)
    act_econ = models.IntegerField(blank=True, null=True)
    estadoactualizacion = models.IntegerField(db_column='EstadoActualizacion', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    reportado_agrodatai = models.BooleanField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    idclientefintech = models.CharField(db_column='IdClienteFintech', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'beneficiarios'

class Tiposorigensolicitudes(models.Model):
    idorigen = models.AutoField(db_column='IdOrigen', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposOrigenSolicitudes'
        
class Tiposfondeo(models.Model):
    idtipofondeo = models.AutoField(db_column='IdTipoFondeo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposFondeo'
       
class Lineasnegocio(models.Model):
    idlineanegocio = models.AutoField(db_column='IdLineaNegocio', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=70, blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LineasNegocio'

class LineasCredito(models.Model):
    id_linea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    usuario_id = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineas_credito'
    
class SolEstados(models.Model):
    sol_estado = models.IntegerField(primary_key=True)
    sol_estado_nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sol_estados'

class SolicitudesTipos(models.Model):
    solic_tipo_id = models.AutoField(primary_key=True)
    solic_tipo_nombre = models.CharField(max_length=50, blank=True, null=True)
    prefijo = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudes_tipos'
        
class BeneficiariosSolicitudes(models.Model):
    benef_solic_id = models.AutoField(primary_key=True)
    idcliente = models.DecimalField(db_column='IdCliente', max_digits=28, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    idcultivo = models.IntegerField(db_column='IdCultivo', blank=True, null=True)  # Field name made lowercase.
    id_linea = models.ForeignKey('LineasCredito', models.DO_NOTHING, db_column='id_linea', blank=True, null=True)
    usuario_id = models.IntegerField(blank=True, null=True)
    usuario_id_solic = models.IntegerField(blank=True, null=True)
    usuario_id_tmp = models.IntegerField(blank=True, null=True)
    benef = models.ForeignKey(Beneficiarios, models.DO_NOTHING, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    fecha_estado = models.DateTimeField(blank=True, null=True)
    solic_estado_id = models.IntegerField(blank=True, null=True)
    solic_tipo = models.ForeignKey('SolicitudesTipos', models.DO_NOTHING, blank=True, null=True)
    visita_previa = models.IntegerField(blank=True, null=True)
    no_credito = models.FloatField(blank=True, null=True)
    no_icr = models.CharField(max_length=50, blank=True, null=True)
    llave_redescto = models.CharField(max_length=30, blank=True, null=True)
    vr_comision_suc = models.FloatField(blank=True, null=True)
    vr_proyecto = models.FloatField(blank=True, null=True)
    vr_credito = models.FloatField(blank=True, null=True)
    vr_activos = models.CharField(max_length=30, blank=True, null=True)
    fecha_inscripcion = models.DateTimeField(blank=True, null=True)
    prorroga = models.IntegerField(blank=True, null=True)
    diasprorroga = models.IntegerField(db_column='DiasProrroga', blank=True, null=True)  # Field name made lowercase.
    idcausalprorroga = models.IntegerField(db_column='IdCausalProrroga', blank=True, null=True)  # Field name made lowercase.
    sol_estado = models.ForeignKey('SolEstados', models.DO_NOTHING, db_column='sol_estado', blank=True, null=True)
    elaborado_cebar = models.IntegerField(blank=True, null=True)
    autorizacion_debito = models.CharField(max_length=70, blank=True, null=True)
    contrato_servicio = models.CharField(max_length=70, blank=True, null=True)
    py_productivo = models.CharField(max_length=70, blank=True, null=True)
    benef_solic_id_padre = models.IntegerField(blank=True, null=True)
    accion_comercial = models.CharField(max_length=50, blank=True, null=True)
    idmunicipio = models.IntegerField(db_column='IdMunicipio', blank=True, null=True)  # Field name made lowercase.
    idsolicitudbanco = models.CharField(db_column='IdSolicitudBanco', max_length=30, blank=True, null=True)  # Field name made lowercase.
    consecutivobanco = models.IntegerField(db_column='consecutivoBanco', blank=True, null=True)  # Field name made lowercase.
    formapago = models.IntegerField(db_column='FormaPago', blank=True, null=True)  # Field name made lowercase.
    fechapago = models.DateField(db_column='FechaPago', blank=True, null=True)  # Field name made lowercase.
    contratofisico = models.IntegerField(db_column='ContratoFisico', blank=True, null=True)  # Field name made lowercase.
    usrcontrato = models.IntegerField(db_column='UsrContrato', blank=True, null=True)  # Field name made lowercase.
    fechacontrato = models.DateTimeField(db_column='FechaContrato', blank=True, null=True)  # Field name made lowercase.
    objetoicr = models.IntegerField(db_column='ObjetoIcr', blank=True, null=True)  # Field name made lowercase.
    desctocomision = models.FloatField(db_column='DesctoComision', blank=True, null=True)  # Field name made lowercase.
    estadoicr = models.CharField(db_column='EstadoIcr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idusuario = models.BigIntegerField(db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    fecharegistroapoyocomercial = models.DateTimeField(db_column='FechaRegistroApoyoComercial', blank=True, null=True)  # Field name made lowercase.
    obsapoyocomercial = models.CharField(db_column='ObsApoyoComercial', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_origen = models.ForeignKey(Tiposorigensolicitudes, models.DO_NOTHING, db_column='id_origen', blank=True, null=True)
    fechadesembolso = models.DateField(db_column='FechaDesembolso', blank=True, null=True)  # Field name made lowercase.
    solicitaseguro = models.BooleanField(db_column='SolicitaSeguro')  # Field name made lowercase.
    idestadoseguro = models.IntegerField(db_column='IdEstadoSeguro', blank=True, null=True)  # Field name made lowercase.
    fechalimitepreaprobado = models.DateField(db_column='FechaLimitePreAprobado', blank=True, null=True)  # Field name made lowercase.
    fechaactualizadesembolso = models.DateTimeField(db_column='FechaActualizaDesembolso', blank=True, null=True)  # Field name made lowercase.
    idtipofondeo = models.ForeignKey(Tiposfondeo, models.DO_NOTHING, db_column='IdTipoFondeo', blank=True, null=True)  # Field name made lowercase.
    idlineanegocio = models.ForeignKey(Lineasnegocio, models.DO_NOTHING, db_column='IdLineaNegocio', blank=True, null=True)  # Field name made lowercase.
    iddestinoinversion = models.IntegerField(db_column='IdDestinoInversion', blank=True, null=True)  # Field name made lowercase.
    idsolicitudfintech = models.CharField(db_column='IdSolicitudFintech', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'beneficiarios_solicitudes'
        
class vwSolicitudes(models.Model):
    tiposolicitud = models.CharField(max_length=255)  # varchar
    nosolicitud = models.IntegerField(primary_key=True)  # int
    idsolicitudbanco = models.CharField(max_length=255)  # nvarchar
    clientenombre = models.CharField(max_length=255)  # varchar
    clienteidentificacion = models.DecimalField(max_digits=20, decimal_places=0)  # numeric
    tipoidentificacion = models.CharField(max_length=255)  # varchar
    telefonofijo = models.CharField(max_length=255)  # varchar
    telefonocelular = models.CharField(max_length=255)  # varchar
    clienteemail = models.CharField(max_length=255)  # varchar
    asesornombre = models.CharField(max_length=255)  # varchar
    fechaultestado = models.DateTimeField()  # datetime
    vr_proyecto = models.FloatField()  # float
    vr_credito = models.FloatField()  # float
    vr_activos = models.CharField(max_length=255)  # varchar
    gerentenombre = models.CharField(max_length=255)  # varchar
    nom_sucursal = models.CharField(max_length=255)  # varchar
    gerenteemail = models.CharField(max_length=255)  # varchar
    nombreregional = models.CharField(max_length=255)  # varchar
    nombrezona = models.CharField(max_length=255)  # varchar
    causaldevinterna = models.TextField()  # text
    fechadevinterna = models.DateTimeField()  # datetime
    fecharadicacion = models.DateTimeField()  # datetime
    fecha_solicitud = models.DateTimeField()  # datetime
    ciudad_nombre = models.CharField(max_length=255)  # nvarchar
    depto_nombre = models.CharField(max_length=255)  # varchar
    accion_comercial = models.CharField(max_length=255)  # varchar
    fecharegistroapoyocomercial = models.DateTimeField()  # datetime
    obsapoyocomercial = models.CharField(max_length=255)  # varchar
    solic_estado_id = models.IntegerField()  # int
    sol_estado = models.IntegerField()  # int
    solic_tipo_id = models.IntegerField()  # int
    idasesor = models.IntegerField()  # int
    codigomunicipio = models.CharField(max_length=255)  # nvarchar
    benef_id = models.IntegerField()  # int
    lineacredito = models.CharField(max_length=255)  # varchar
    fechadesembolso = models.DateField()  # date
    origensolicitud = models.CharField(max_length=255)  # varchar
    tasa_cliente = models.FloatField()  # float
    vr_comision_cliente = models.FloatField()  # float
    tasa_asesor = models.FloatField()  # float
    vr_comision_asesor = models.FloatField()  # float
    vr_py = models.FloatField()  # float
    vr_inv = models.FloatField()  # float
    codigo_id = models.IntegerField()  # int
    rubro_id = models.IntegerField()  # int
    pla_tot_meses = models.IntegerField()  # int
    rubro_nombre = models.CharField(max_length=255)  # varchar
    analistanombre = models.CharField(max_length=255)  # varchar
    destinoinversion = models.CharField(max_length=255)  # nvarchar
    tipoproductor = models.CharField(max_length=255)  # nvarchar
    tipoproduccion = models.CharField(max_length=255)  # varchar
    has = models.FloatField()  # float
    linea = models.CharField(max_length=255)  # varchar
    per_gra_meses = models.IntegerField()  # int
    actividadeconomica = models.CharField(max_length=255)  # varchar
    negocionombre = models.CharField(max_length=255)  # varchar
    direccioncliente = models.CharField(max_length=255)  # varchar
    benef_celular2 = models.CharField(max_length=255)  # varchar
    benef_celular3 = models.CharField(max_length=255)  # varchar
    benef_email2 = models.CharField(max_length=255)  # varchar
    comercial = models.CharField(max_length=255)  # varchar
    actividad_solicitud = models.CharField(max_length=255)  # varchar
    solic_estado_nombre = models.CharField(max_length=255)  # varchar
    fortografiaspy = models.IntegerField()  # int
    tipobeneficiario = models.CharField(max_length=255)  # varchar

    class Meta:
        managed = False
        db_table = 'vw_ConsultaYisedFormatoVEProyectoAgrop_2'

class VwSolicitudesVigentes(models.Model):
    TipoSolicitud = models.CharField(max_length=255)
    NoSolicitud = models.IntegerField(primary_key=True)
    IdSolicitudBanco = models.CharField(max_length=255)
    ClienteNombre = models.CharField(max_length=255)
    ClienteIdentificacion = models.DecimalField(max_digits=18, decimal_places=0)
    TipoIdentificacion = models.CharField(max_length=255)
    TelefonoFijo = models.CharField(max_length=255)
    TelefonoCelular = models.CharField(max_length=255)
    ClienteEmail = models.EmailField()
    AsesorNombre = models.CharField(max_length=255)
    FechaUltEstado = models.DateTimeField()
    vr_proyecto = models.FloatField()
    vr_credito = models.FloatField()
    vr_activos = models.CharField(max_length=255)
    GerenteNombre = models.CharField(max_length=255)
    nom_sucursal = models.CharField(max_length=255)
    GerenteEmail = models.EmailField()
    NombreRegional = models.CharField(max_length=255)
    NombreZona = models.CharField(max_length=255)
    CausalDevInterna = models.TextField()
    FechaDevInterna = models.DateTimeField()
    FechaRadicacion = models.DateTimeField()
    fecha_solicitud = models.DateTimeField()
    ciudad_nombre = models.CharField(max_length=255)
    depto_nombre = models.CharField(max_length=255)
    accion_comercial = models.CharField(max_length=255)
    FechaRegistroApoyoComercial = models.DateTimeField()
    ObsApoyoComercial = models.CharField(max_length=255)
    solic_estado_id = models.IntegerField()
    sol_estado = models.IntegerField()
    solic_tipo_id = models.IntegerField()
    IdAsesor = models.IntegerField()
    CodigoMunicipio = models.CharField(max_length=255)
    benef_id = models.IntegerField()
    LineaCredito = models.CharField(max_length=255)
    FechaDesembolso = models.DateField()
    OrigenSolicitud = models.CharField(max_length=255)
    tasa_cliente = models.FloatField()
    vr_comision_cliente = models.FloatField()
    tasa_asesor = models.FloatField()
    vr_comision_asesor = models.FloatField()
    vr_py = models.FloatField()
    vr_inv = models.FloatField()
    codigo_id = models.IntegerField()
    rubro_id = models.IntegerField()
    pla_tot_meses = models.IntegerField()
    rubro_nombre = models.CharField(max_length=255)
    AnalistaNombre = models.CharField(max_length=255)
    DestinoInversion = models.CharField(max_length=255)
    TipoProductor = models.CharField(max_length=255)
    TipoProduccion = models.CharField(max_length=255)
    Has = models.FloatField()
    Linea = models.CharField(max_length=255)
    per_gra_meses = models.IntegerField()
    ActividadEconomica = models.CharField(max_length=255)
    NegocioNombre = models.CharField(max_length=255)
    DireccionCliente = models.CharField(max_length=255)
    benef_celular2 = models.CharField(max_length=255)
    benef_celular3 = models.CharField(max_length=255)
    benef_email2 = models.EmailField()
    comercial = models.CharField(max_length=255)
    actividad_solicitud = models.CharField(max_length=255)
    solic_estado_nombre = models.CharField(max_length=255)
    FortografiasPy = models.IntegerField()
    TipoBeneficiario = models.CharField(max_length=255)
    FECHAFIN = models.DateField()
    DIAS_VENCIMIENTO = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'VW_DESEMBOLSOS_ACTIVOS'