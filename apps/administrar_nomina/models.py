from django.db import models


Estado = [
    ("Activo","Activo"),
    ("Inactivo","Inactivo"),
]

Valor_parafiscales = [

    ("2","2"),
    ("3","3"),
    ("4","4"),
]

Descripcion_vinculacion = [

    ("Vinculado","Vinculado"),
    ("Desvinculado","Desvinculado"),
]

# Create your models here.
class Cargo(models.Model):
        Id_cargo=models.AutoField( primary_key=True)
        Nombre=models.CharField(max_length=50)
        Estado=models.CharField(max_length=50, null=True, blank=True, choices=Estado,default="Activo")
        Valor_cargo=models.CharField(max_length=50)
        
def __str__(self):
    return '{} {} {} {}'.format(self.Id_cargo,self.Nombre,self.Estado,self.Valor_cargo)

def save(self, *args, **kwargs):
      if  not self.CharField:
         self.CharField = float(self.Nombre)
      super(Cargo, self), save(*args,**kwargs)



class Tipo_vinculacion(models.Model):
        Id_tipo_vinculacion=models.AutoField( primary_key=True)
        Descripcion_vinculacion=models.CharField(max_length=50, null=True, blank=True, choices=Descripcion_vinculacion,default="Vinculado")
        Estado=models.CharField(max_length=50, null=True, blank=True, choices=Estado,default="Activo")
def __str__(self):
    return '{} {} {}'.format(self.Id_tipo_vinculacion,self.Descripcion_vinculacion,self.Estado)

class Empleado(models.Model):
      Id_empleado=models.AutoField( primary_key=True)
      Nombre=models.CharField(max_length=50)
      Apellido=models.CharField(max_length=50)
      Email=models.EmailField()
      Telefono=models.CharField(max_length=50)
      Documento=models.CharField(max_length=50)
      Tipo_documento=models.CharField(max_length=50)
      Id_cargo=models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)
      Id_tipo_vinculacion=models.ForeignKey(Tipo_vinculacion, null=True, blank=True, on_delete=models.CASCADE)
      Estado=models.CharField(max_length=50, null=True, blank=True, choices=Estado,default="Activo")
def __str__(self):
    return '{} {} {} {} {} {} {} {} {} {}'.format(self.Id_empleado,self.Nombre,self.Apellido,self.Email,self.Telefono,self.Documento,self.Tipo_documento,self.Id_cargo,self.Id_tipo_vinculacion,self.Estado)

class Parafiscales(models.Model):
        Id_parafiscales=models.AutoField( primary_key=True)
        Nombre=models.CharField(max_length=50)
        Valor_parafiscales=models.CharField(max_length=50, null=True, blank=True, choices=Valor_parafiscales,default="3")
        Estado=models.CharField(max_length=50, null=True, blank=True, choices=Estado,default="Activo")
        Id_tipo_vinculacion=models.ForeignKey(Tipo_vinculacion, null=True, blank=True, on_delete=models.CASCADE)
def __str__(self):
    return '{} {} {} {} {}'.format(self.Id_parafiscales,self.Nombre,self.Valor_parafiscales,self.Estado,self.Id_tipo_vinculacion)

class Periodo(models.Model):
    Id_periodo=models.AutoField( primary_key=True)
    Anual=models.DateField()
    Mes=models.DateField()
def __str__(self):
    return '{} {} {}'.format(self.Id_periodo,self.Anual,self.Mes)

class Nomina(models.Model):
    Id_nomina=models.AutoField( primary_key=True)
    Valor_pagar=models.CharField(max_length=50)
    Subtotal=models.CharField(max_length=50)
    Id_periodo=models.ForeignKey(Periodo, null=True, blank=True, on_delete=models.CASCADE)
    Id_empleado=models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    Pago=models.CharField(max_length=50)
    Estado=models.CharField(max_length=50, null=True, blank=True, choices=Estado,default="Activo")
def __str__(self):
    return '{} {} {} {} {} {} {}'.format(self.Id_nomina,self.Valor_pagar,self.Subtotal,self.Id_periodo,self.Id_empleado,self.Pago,self.Estado)

class Detalle_parafiscales(models.Model):
        Id_detalle_parafiscales=models.AutoField( primary_key=True)
        Id_nomina=models.ForeignKey(Nomina, null=True, blank=True, on_delete=models.CASCADE)
        Total_parafiscales=models.CharField(max_length=50)
        Id_parafiscales=models.ForeignKey(Parafiscales, null=True, blank=True, on_delete=models.CASCADE)
def __str__(self):
    return '{} {} {} {}'.format(self.Id_detalle_parafiscales,self.Id_nomina,self.Total_parafiscales,self.Id_parafiscales)

class Reporte_horas(models.Model):
    Id_reporte_horas=models.AutoField( primary_key=True)
    Id_empleado=models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    Id_periodo=models.ForeignKey(Periodo, null=True, blank=True, on_delete=models.CASCADE)
    Numero_horas=models.CharField(max_length=50)
def __str__(self):
    return '{} {} {} {}'.format(self.Id_reporte_horas,self.Id_empleado,self.Id_periodo,self.Numero_horas)

class Detalle_horas(models.Model):
        Id_detalle_horas=models.AutoField( primary_key=True)
        Id_nomina=models.ForeignKey(Nomina, null=True, blank=True, on_delete=models.CASCADE)
        Total=models.CharField(max_length=50)
        Cantidad=models.CharField(max_length=50)  
def __str__(self):
    return '{} {} {} {}'.format(self.Id_detalle_horas,self.Id_nomina,self.Total,self.Cantidad)

class Horas_extras(models.Model):
        Id_horas_extras=models.AutoField( primary_key=True)
        Nombre=models.CharField(max_length=50)
        Valor_hora_extra=models.CharField(max_length=50)
        Estado=models.CharField(max_length=50, null=True, blank=True, choices=Estado,default="Activo")
        Id_detalle_horas=models.ForeignKey(Detalle_horas, null=True, blank=True, on_delete=models.CASCADE)
def __str__(self):
    return '{} {} {} {} {}'.format(self.Id_horas_extras,self.Nombre,self.Valor_hora_extra,self.Estado,self.Id_detalle_horas)

