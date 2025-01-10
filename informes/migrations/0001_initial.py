# Generated by Django 5.0.10 on 2025-01-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiarios',
            fields=[
                ('benef_id', models.AutoField(primary_key=True, serialize=False)),
                ('benef_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('benef_primer_nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('benef_segundo_nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('benef_primer_apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('benef_segundo_apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('benef_direccion', models.CharField(blank=True, max_length=80, null=True)),
                ('benef_telefono', models.CharField(blank=True, max_length=40, null=True)),
                ('benef_celular', models.CharField(blank=True, max_length=50, null=True)),
                ('benef_celular2', models.CharField(blank=True, max_length=50, null=True)),
                ('benef_celular3', models.CharField(blank=True, max_length=50, null=True)),
                ('benef_email', models.CharField(blank=True, max_length=90, null=True)),
                ('benef_email2', models.CharField(blank=True, max_length=90, null=True)),
                ('benef_email3', models.CharField(blank=True, max_length=90, null=True)),
                ('benef_web', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad_id', models.IntegerField(blank=True, null=True)),
                ('depto_id', models.IntegerField(blank=True, null=True)),
                ('benef_ident_no', models.DecimalField(blank=True, decimal_places=0, max_digits=28, null=True)),
                ('div', models.IntegerField(blank=True, null=True)),
                ('usuario_id', models.IntegerField(blank=True, null=True)),
                ('benef_fecha', models.DateTimeField(blank=True, null=True)),
                ('benef_observaciones', models.TextField(blank=True, null=True)),
                ('tipo_persona', models.IntegerField(blank=True, null=True)),
                ('idclientecrm', models.BigIntegerField(blank=True, null=True)),
                ('int_benef_id', models.IntegerField(blank=True, null=True)),
                ('act_agro', models.IntegerField(blank=True, null=True)),
                ('act_econ', models.IntegerField(blank=True, null=True)),
                ('estadoactualizacion', models.IntegerField(blank=True, db_column='EstadoActualizacion', null=True)),
                ('estado', models.IntegerField(blank=True, db_column='Estado', null=True)),
                ('reportado_agrodatai', models.BooleanField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('idclientefintech', models.CharField(blank=True, db_column='IdClienteFintech', max_length=50, null=True)),
            ],
            options={
                'db_table': 'beneficiarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BeneficiariosSolicitudes',
            fields=[
                ('benef_solic_id', models.AutoField(primary_key=True, serialize=False)),
                ('idcliente', models.DecimalField(blank=True, db_column='IdCliente', decimal_places=0, max_digits=28, null=True)),
                ('idcultivo', models.IntegerField(blank=True, db_column='IdCultivo', null=True)),
                ('usuario_id', models.IntegerField(blank=True, null=True)),
                ('usuario_id_solic', models.IntegerField(blank=True, null=True)),
                ('usuario_id_tmp', models.IntegerField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_solicitud', models.DateTimeField(blank=True, null=True)),
                ('fecha_estado', models.DateTimeField(blank=True, null=True)),
                ('solic_estado_id', models.IntegerField(blank=True, null=True)),
                ('visita_previa', models.IntegerField(blank=True, null=True)),
                ('no_credito', models.FloatField(blank=True, null=True)),
                ('no_icr', models.CharField(blank=True, max_length=50, null=True)),
                ('llave_redescto', models.CharField(blank=True, max_length=30, null=True)),
                ('vr_comision_suc', models.FloatField(blank=True, null=True)),
                ('vr_proyecto', models.FloatField(blank=True, null=True)),
                ('vr_credito', models.FloatField(blank=True, null=True)),
                ('vr_activos', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_inscripcion', models.DateTimeField(blank=True, null=True)),
                ('prorroga', models.IntegerField(blank=True, null=True)),
                ('diasprorroga', models.IntegerField(blank=True, db_column='DiasProrroga', null=True)),
                ('idcausalprorroga', models.IntegerField(blank=True, db_column='IdCausalProrroga', null=True)),
                ('elaborado_cebar', models.IntegerField(blank=True, null=True)),
                ('autorizacion_debito', models.CharField(blank=True, max_length=70, null=True)),
                ('contrato_servicio', models.CharField(blank=True, max_length=70, null=True)),
                ('py_productivo', models.CharField(blank=True, max_length=70, null=True)),
                ('benef_solic_id_padre', models.IntegerField(blank=True, null=True)),
                ('accion_comercial', models.CharField(blank=True, max_length=50, null=True)),
                ('idmunicipio', models.IntegerField(blank=True, db_column='IdMunicipio', null=True)),
                ('idsolicitudbanco', models.CharField(blank=True, db_column='IdSolicitudBanco', max_length=30, null=True)),
                ('consecutivobanco', models.IntegerField(blank=True, db_column='consecutivoBanco', null=True)),
                ('formapago', models.IntegerField(blank=True, db_column='FormaPago', null=True)),
                ('fechapago', models.DateField(blank=True, db_column='FechaPago', null=True)),
                ('contratofisico', models.IntegerField(blank=True, db_column='ContratoFisico', null=True)),
                ('usrcontrato', models.IntegerField(blank=True, db_column='UsrContrato', null=True)),
                ('fechacontrato', models.DateTimeField(blank=True, db_column='FechaContrato', null=True)),
                ('objetoicr', models.IntegerField(blank=True, db_column='ObjetoIcr', null=True)),
                ('desctocomision', models.FloatField(blank=True, db_column='DesctoComision', null=True)),
                ('estadoicr', models.CharField(blank=True, db_column='EstadoIcr', max_length=50, null=True)),
                ('idusuario', models.BigIntegerField(blank=True, db_column='IdUsuario', null=True)),
                ('fecharegistroapoyocomercial', models.DateTimeField(blank=True, db_column='FechaRegistroApoyoComercial', null=True)),
                ('obsapoyocomercial', models.CharField(blank=True, db_column='ObsApoyoComercial', max_length=200, null=True)),
                ('fechadesembolso', models.DateField(blank=True, db_column='FechaDesembolso', null=True)),
                ('solicitaseguro', models.BooleanField(db_column='SolicitaSeguro')),
                ('idestadoseguro', models.IntegerField(blank=True, db_column='IdEstadoSeguro', null=True)),
                ('fechalimitepreaprobado', models.DateField(blank=True, db_column='FechaLimitePreAprobado', null=True)),
                ('fechaactualizadesembolso', models.DateTimeField(blank=True, db_column='FechaActualizaDesembolso', null=True)),
                ('iddestinoinversion', models.IntegerField(blank=True, db_column='IdDestinoInversion', null=True)),
                ('idsolicitudfintech', models.CharField(blank=True, db_column='IdSolicitudFintech', max_length=50, null=True)),
            ],
            options={
                'db_table': 'beneficiarios_solicitudes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LineasCredito',
            fields=[
                ('id_linea', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('usuario_id', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lineas_credito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lineasnegocio',
            fields=[
                ('idlineanegocio', models.AutoField(db_column='IdLineaNegocio', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=70, null=True)),
                ('estado', models.BooleanField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'LineasNegocio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolEstados',
            fields=[
                ('sol_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('sol_estado_nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sol_estados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolicitudesTipos',
            fields=[
                ('solic_tipo_id', models.AutoField(primary_key=True, serialize=False)),
                ('solic_tipo_nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('prefijo', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'solicitudes_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposBeneficiarios',
            fields=[
                ('tipo_benef_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_benef_nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('montoactivos', models.BigIntegerField(blank=True, db_column='MontoActivos', null=True)),
                ('idtipoproductor', models.IntegerField(blank=True, db_column='IdTipoProductor', null=True)),
            ],
            options={
                'db_table': 'tipos_beneficiarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiposfondeo',
            fields=[
                ('idtipofondeo', models.AutoField(db_column='IdTipoFondeo', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
                ('estado', models.BooleanField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'TiposFondeo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposIdentificacion',
            fields=[
                ('tipo_ident_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_ident_nombre', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'tipos_identificacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiposorigensolicitudes',
            fields=[
                ('idorigen', models.AutoField(db_column='IdOrigen', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=30, null=True)),
                ('estado', models.BooleanField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'TiposOrigenSolicitudes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='vwSolicitudes',
            fields=[
                ('tiposolicitud', models.CharField(max_length=255)),
                ('nosolicitud', models.IntegerField(primary_key=True, serialize=False)),
                ('idsolicitudbanco', models.CharField(max_length=255)),
                ('clientenombre', models.CharField(max_length=255)),
                ('clienteidentificacion', models.DecimalField(decimal_places=0, max_digits=20)),
                ('tipoidentificacion', models.CharField(max_length=255)),
                ('telefonofijo', models.CharField(max_length=255)),
                ('telefonocelular', models.CharField(max_length=255)),
                ('clienteemail', models.CharField(max_length=255)),
                ('asesornombre', models.CharField(max_length=255)),
                ('fechaultestado', models.DateTimeField()),
                ('vr_proyecto', models.FloatField()),
                ('vr_credito', models.FloatField()),
                ('vr_activos', models.CharField(max_length=255)),
                ('gerentenombre', models.CharField(max_length=255)),
                ('nom_sucursal', models.CharField(max_length=255)),
                ('gerenteemail', models.CharField(max_length=255)),
                ('nombreregional', models.CharField(max_length=255)),
                ('nombrezona', models.CharField(max_length=255)),
                ('causaldevinterna', models.TextField()),
                ('fechadevinterna', models.DateTimeField()),
                ('fecharadicacion', models.DateTimeField()),
                ('fecha_solicitud', models.DateTimeField()),
                ('ciudad_nombre', models.CharField(max_length=255)),
                ('depto_nombre', models.CharField(max_length=255)),
                ('accion_comercial', models.CharField(max_length=255)),
                ('fecharegistroapoyocomercial', models.DateTimeField()),
                ('obsapoyocomercial', models.CharField(max_length=255)),
                ('solic_estado_id', models.IntegerField()),
                ('sol_estado', models.IntegerField()),
                ('solic_tipo_id', models.IntegerField()),
                ('idasesor', models.IntegerField()),
                ('codigomunicipio', models.CharField(max_length=255)),
                ('benef_id', models.IntegerField()),
                ('lineacredito', models.CharField(max_length=255)),
                ('fechadesembolso', models.DateField()),
                ('origensolicitud', models.CharField(max_length=255)),
                ('tasa_cliente', models.FloatField()),
                ('vr_comision_cliente', models.FloatField()),
                ('tasa_asesor', models.FloatField()),
                ('vr_comision_asesor', models.FloatField()),
                ('vr_py', models.FloatField()),
                ('vr_inv', models.FloatField()),
                ('codigo_id', models.IntegerField()),
                ('rubro_id', models.IntegerField()),
                ('pla_tot_meses', models.IntegerField()),
                ('rubro_nombre', models.CharField(max_length=255)),
                ('analistanombre', models.CharField(max_length=255)),
                ('destinoinversion', models.CharField(max_length=255)),
                ('tipoproductor', models.CharField(max_length=255)),
                ('tipoproduccion', models.CharField(max_length=255)),
                ('has', models.FloatField()),
                ('linea', models.CharField(max_length=255)),
                ('per_gra_meses', models.IntegerField()),
                ('actividadeconomica', models.CharField(max_length=255)),
                ('negocionombre', models.CharField(max_length=255)),
                ('direccioncliente', models.CharField(max_length=255)),
                ('benef_celular2', models.CharField(max_length=255)),
                ('benef_celular3', models.CharField(max_length=255)),
                ('benef_email2', models.CharField(max_length=255)),
                ('comercial', models.CharField(max_length=255)),
                ('actividad_solicitud', models.CharField(max_length=255)),
                ('solic_estado_nombre', models.CharField(max_length=255)),
                ('fortografiaspy', models.IntegerField()),
                ('tipobeneficiario', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vw_ConsultaYisedFormatoVEProyectoAgrop_2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'contact_try',
            },
        ),
    ]
