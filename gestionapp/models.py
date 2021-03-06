from django.db import models

# Create your models here.

COLORES = (
    ('0', 'Blanco'),
    ('1', 'Negro'),
    ('2', 'Rojo'),
    ('3', 'Amarillo'),
    ('4', 'Azul'),
)


class Camposcomunes_masterdoc(models.Model):
    codigo = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=30, null=True, blank=True)
    tipdoc = models.CharField(max_length=30, null=True, blank=True)
    destipdoc = models.CharField(max_length=30, null=True, blank=True)
    seriedoc = models.CharField(max_length=30, null=True, blank=True)
    numerodoc = models.CharField(max_length=30, null=True, blank=True)
    fechadoc = models.DateField(null=True, blank=True)
    fecentrega = models.DateField(null=True, blank=True)  # Fecha entrega pedido
    ruc = models.CharField(max_length=30, null=True, blank=True)
    desruc = models.CharField(max_length=150, null=True, blank=True)
    telruc = models.CharField(max_length=30, null=True, blank=True)
    paisruc = models.CharField(max_length=30, null=True, blank=True)
    dptoruc = models.CharField(max_length=30, null=True, blank=True)
    provruc = models.CharField(max_length=30, null=True, blank=True)
    distruc = models.CharField(max_length=30, null=True, blank=True)
    codpostalruc = models.CharField(max_length=30, null=True, blank=True)
    dirruc = models.CharField(max_length=150, null=True, blank=True)
    conpag = models.CharField(max_length=30, null=True, blank=True)
    desconpag = models.CharField(max_length=50, null=True, blank=True)
    monedapago = models.IntegerField(default=0)  # soles,dolares,euros,yen
    desmonepago = models.CharField(max_length=50, null=True, blank=True)
    tc_dolares = models.IntegerField(default=0)
    tc_euros = models.IntegerField(default=0)
    tc_yen = models.IntegerField(default=0)
    numeroguia = models.IntegerField(default=0)
    numordserv = models.IntegerField(default=0)
    vendidopor = models.CharField(max_length=30, null=True, blank=True)
    fechapago = models.DateField(null=True, blank=True)
    unidadtransporte = models.CharField(max_length=50, null=True, blank=True)
    autorizadosunat = models.IntegerField(default=0)
    impsubtotal = models.IntegerField(default=0)
    impanticipos = models.IntegerField(default=0)
    impdescuentos = models.IntegerField(default=0)
    impvalorventa = models.IntegerField(default=0)
    impisc = models.IntegerField(default=0)
    impigv = models.IntegerField(default=0)
    nvaligv = models.IntegerField(default=0)
    impotroscargos = models.IntegerField(default=0)
    impotrostributos = models.IntegerField(default=0)
    imptotal = models.IntegerField(default=0)
    cc1 = models.CharField(max_length=30, null=True, blank=True)  # cc para saber donde se hace gasto
    cc2 = models.CharField(max_length=30, null=True, blank=True)
    cc3 = models.CharField(max_length=30, null=True, blank=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    correoruc = models.CharField(max_length=150, null=True, blank=True)
    horaini = models.CharField(max_length=30, null=True, blank=True)
    horafin = models.CharField(max_length=30, null=True, blank=True)
    lugorigen = models.CharField(max_length=50, null=True, blank=True)
    lugdestino = models.CharField(max_length=50, null=True, blank=True)
    opcviaje = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        abstract = True


class Camposcomunes_detaildoc(models.Model):
    codigo = models.IntegerField(default=0)
    codpro = models.CharField(max_length=30, null=True, blank=True)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    unimed = models.CharField(max_length=60, null=True, blank=True)
    desunimed = models.CharField(max_length=60, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    precio = models.IntegerField(default=0, null=True, blank=True)
    impsubtotal = models.IntegerField(default=0, null=True, blank=True)
    impanticipos = models.IntegerField(default=0, null=True, blank=True)
    impdescuentos = models.IntegerField(default=0, null=True, blank=True)
    impvalorventa = models.IntegerField(default=0, null=True, blank=True)
    impisc = models.IntegerField(default=0, null=True, blank=True)
    impigv = models.IntegerField(default=0, null=True, blank=True)
    nvaligv = models.IntegerField(default=0, null=True, blank=True)
    impotroscargos = models.IntegerField(default=0, null=True, blank=True)
    impotrostributos = models.IntegerField(default=0, null=True, blank=True)
    imptotal = models.IntegerField(default=0, null=True, blank=True)
    desgrupo1 = models.CharField(max_length=30, null=True, blank=True)
    desgrupo2 = models.CharField(max_length=30, null=True, blank=True)
    cc1 = models.CharField(max_length=30, null=True, blank=True)  # cc para saber donde se hace gasto
    cc2 = models.CharField(max_length=30, null=True, blank=True)
    cc3 = models.CharField(max_length=30, null=True, blank=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    horaini = models.CharField(max_length=30, null=True, blank=True)
    horafin = models.CharField(max_length=30, null=True, blank=True)
    lugorigen = models.CharField(max_length=50, null=True, blank=True)
    lugdestino = models.CharField(max_length=50, null=True, blank=True)
    opcviaje = models.CharField(max_length=30, null=True, blank=True)
    estado = models.ForeignKey('CotizacionEstado', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Camposcomunes_auditoria(models.Model):
    sucursal = models.CharField(max_length=10, blank=True, null=True)
    estado = models.IntegerField(default=0)
    anulado = models.IntegerField(default=0)
    fecregistro = models.DateField(null=True, blank=True)
    aud_idusu = models.CharField(max_length=30, blank=True, null=True)
    aud_feccre = models.DateTimeField(auto_now=True)
    aud_fecmod = models.DateField(null=True, blank=True)
    aud_feceli = models.DateField(null=True, blank=True)
    posmapa = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Camposcomunes_personal(models.Model):
    codigo = models.CharField(max_length=15, blank=True, null=True)
    ruc = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    telefono3 = models.CharField(max_length=20, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telcontacto = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)
    paginaweb = models.CharField(max_length=150, blank=True, null=True)
    tipocc = models.IntegerField(default=0, blank=True, null=True)
    destipocc = models.CharField(max_length=100, blank=True, null=True)
    condcompvent = models.CharField(max_length=100, blank=True, null=True)
    banco_nombre1 = models.CharField(max_length=100, blank=True, null=True)
    banco_cuenta1 = models.CharField(max_length=100, blank=True, null=True)
    banco_moneda1 = models.CharField(max_length=20, blank=True, null=True)
    banco_nombre2 = models.CharField(max_length=100, blank=True, null=True)
    banco_cuenta2 = models.CharField(max_length=100, blank=True, null=True)
    banco_moneda2 = models.CharField(max_length=20, blank=True, null=True)
    fechanac = models.DateField(null=True, blank=True, help_text="Ingrese si esta activo u otro stado ")
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class Deposito(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)


# Unidades de Transporte
class Unidad(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    placa = models.CharField(max_length=30, blank=True, null=True)
    npasajeros = models.CharField(max_length=150, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)


# Programa gastos,Mantenimiento para unidades
class Programagastos(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    unidad = models.CharField(max_length=30, blank=True, null=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)


class Programagasto(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    unidad = models.CharField(max_length=30, blank=True, null=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)


class Articulo(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=60)
    cantidad = models.IntegerField(default=0)
    color = models.CharField(max_length=2, default=0, choices=COLORES)
    deposito = models.ForeignKey(Deposito, null=True, on_delete=models.SET_NULL)
    stock1 = models.IntegerField(default=0)
    codbarra = models.CharField(max_length=60, blank=True, null=True)
    stockalm1 = models.IntegerField(default=0)
    stockalm2 = models.IntegerField(default=0)
    stockalm3 = models.IntegerField(default=0)
    afectoigv = models.IntegerField(default=0)
    preciocosto = models.IntegerField(default=0)
    precioventa = models.IntegerField(default=0)
    aplicadscto = models.IntegerField(default=0)
    cc1 = models.CharField(max_length=60, blank=True, null=True)
    descc1 = models.CharField(max_length=60, blank=True, null=True)


class Centrodecosto1(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    totingresos = models.IntegerField(default=0)
    totgastos = models.IntegerField(default=0)


class Banco(models.Model):
    codigo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)


# centro de costo para monitor de flujo gasto ingreso


class Cliente(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Proveedor(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Transporte(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Chofer(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


# ARCHIVOS DE MOVIMIENTO

class Mcotizacion(Camposcomunes_masterdoc, Camposcomunes_auditoria):
    pass


class Dcotizacion(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    master = models.ForeignKey(Mcotizacion, related_name='cotizaciones', on_delete=models.CASCADE, null=True)


class Mguia(models.Model):
    pass


class Dguia(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    pass


class Mgasto(models.Model):
    pass


class Dgasto(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    pass


class Clientesdireccion(models.Model):
    master = models.ForeignKey(Cliente, related_name='clientesdirecciones', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    class Meta:
        unique_together = ('master', 'id')
        ordering = ['id']

    def __unicode__(self):
        return '%d: %s' % (self.direccion, self.telefono)


class CotizacionEstado(models.Model):
    name = models.CharField(max_length=254)
    color = models.CharField(max_length=100)
