from django import forms
from apps.administrar_nomina.models import Cargo
from apps.administrar_nomina.models import Tipo_vinculacion
from apps.administrar_nomina.models import Empleado
from apps.administrar_nomina.models import Parafiscales
from apps.administrar_nomina.models import Detalle_parafiscales
from apps.administrar_nomina.models import Reporte_horas
from apps.administrar_nomina.models import Detalle_horas
from apps.administrar_nomina.models import Horas_extras
from apps.administrar_nomina.models import Nomina
from apps.administrar_nomina.models import Periodo

from functools import partial
from _datetime import datetime

DateInput = partial(forms.DateInput, {'class':'datapicker'})


class CargoForm(forms.ModelForm):
    class Meta:

        model= Cargo

        fields = [

        'Id_cargo',
        'Nombre',
        'Estado',
        'Valor_cargo',
        ]

        labels = {

        'Id_cargo':'Id cargo',
        'Nombre':'Nombre',
        'Estado':'Estado',
        'Valor_cargo':'Valor cargo',
        }
        widgets = {

        'Id_cargo': forms.TextInput(attrs={'class':'form-control'}),
        'Nombre': forms.TextInput(attrs={'class':'form-control'}),
        'Estado': forms.TextInput(attrs={'class':'form-control'}),
        'Valor_cargo': forms.TextInput(attrs={'class':'form-control', 'name': 'id_Valor_cargo', 'id':'id_Valor_cargo'}),
        }

class Tipo_vinculacionForm(forms.ModelForm):
    class Meta:

        model= Tipo_vinculacion

        fields = [

        'Id_tipo_vinculacion',
        'Descripcion_vinculacion',
        'Estado',
        ]

        labels = {

        'Id_tipo_vinculacion':'Id tipo vinculacion',
        'Descripcion_vinculacion':'descripcion vinculacion',
        'Estado':'Estado',
        }
        widgets = {

        'Id_tipo_vinculacion': forms.TextInput(attrs={'class':'form-control'}),
        'Descripcion_vinculacion': forms.TextInput(attrs={'class':'form-control'}),
        'Estado': forms.TextInput(attrs={'class':'form-control'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:

        model= Empleado

        fields = [

        'Id_empleado',
        'Nombre',
        'Apellido',
        'Email',
        'Telefono',
        'Documento',
        'Tipo_documento',
        'Id_cargo',
        'Id_tipo_vinculacion',
        'Estado',
        ]

        labels = {

        'Id_empleado':'Id empleado',
        'Nombre':'Nombre',
        'Apellido':'Apellido',
        'Email':'Email',
        'Telefono':'Telefono',
        'Documento':'Documento',
        'Tipo_documento':'Tipo de documento',
        'Id_cargo':'Id cargo' ,
        'Id_tipo_vinculacion':'Id tipo vinculacion',
        'Estado':'Estado',
        }
        widgets = {

        'Id_empleado': forms.TextInput(attrs={'class':'form-control'}),
        'Nombre':forms.TextInput(attrs={'class':'form-control'}),
        'Apellido':forms.TextInput(attrs={'class':'form-control'}),
        'Email':forms.EmailInput(attrs={'class':'form-control'}),
        'Telefono':forms.TextInput(attrs={'class':'form-control'}),
        'Documento':forms.TextInput(attrs={'class':'form-control'}),
        'Tipo_documento':forms.TextInput(attrs={'class':'form-control'}),
        'Id_cargo':forms.TextInput(attrs={'class':'form-control'}),
        'Id_tipo_vinculacion':forms.TextInput(attrs={'class':'form-control'}),
        'Estado':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class ParafiscalesForm(forms.ModelForm):
    class Meta:

        model= Parafiscales

        fields = [

        'Id_parafiscales',
        'Nombre',
        'Valor_parafiscales',
        'Estado',
        'Id_tipo_vinculacion',
        ]

        labels = {

        'Id_parafiscales':'Id parafiscal',
        'Nombre':'Nombre',
        'Valor_parafiscales':'Valor parafiscales',
        'Estado':'Estado',
        'Id_tipo_vinculacion':'Id tipo vinculacion',
        }
        widgets = {

        'Id_parafiscales': forms.TextInput(attrs={'class':'form-control'}),
        'Nombre':forms.TextInput(attrs={'class':'form-control'}),
        'Valor_parafiscales':forms.TextInput(attrs={'class':'form-control', 'name': 'id_parafiscales', 'id':'id_parafiscales'}),
        'Estado':forms.TextInput(attrs={'class':'form-control'}),
        'Id_tipo_vinculacion':forms.TextInput(attrs={'class':'form-control'}),
        }

class Detalle_parafiscalesForm(forms.ModelForm):
    class Meta:

        model= Detalle_parafiscales

        fields = [

        'Id_detalle_parafiscales',
        'Id_nomina',
        'Total_parafiscales',
        'Id_parafiscales',
        ]

        labels = {

        'Id_detalle_parafiscales':'Id detalle parafiscales',
        'Id_nomina':'Id nomina',
        'Total_parafiscales':'Total parafiscales',
        'Id_parafiscales':'Id parafiscales',
        }
        widgets = {

         'Id_detalle_parafiscales': forms.TextInput(attrs={'class':'form-control'}),
        'Id_nomina': forms.TextInput(attrs={'class':'form-control'}),
        'Total_parafiscales': forms.TextInput(attrs={'class':'form-control'}),
        'Id_parafiscales': forms.TextInput(attrs={'class':'form-control'}),
        }

class Reporte_horasForm(forms.ModelForm):
    class Meta:

        model= Reporte_horas

        fields = [

         'Id_reporte_horas',
         'Id_empleado',
         'Id_periodo',
         'Numero_horas',
        ]

        labels = {

         'Id_reporte_horas':'Id reporte horas',
         'Id_empleado':'Id empleado',
         'Id_periodo':'Id periodo',
         'Numero_horas':'Numero horas',
        }
        widgets = {

        'Id_reporte_horas': forms.TextInput(attrs={'class':'form-control'}),
        'Id_empleado': forms.TextInput(attrs={'class':'form-control'}),
        'Id_periodo': forms.TextInput(attrs={'class':'form-control'}),
        'Numero_horas': forms.TextInput(attrs={'class':'form-control'}),
        }

class Detalle_horasForm(forms.ModelForm):
    class Meta:

        model= Detalle_horas

        fields = [

         'Id_detalle_horas',
         'Id_nomina',
         'Total',
         'Cantidad',
        ]

        labels = {

         'Id_detalle_horas':'Id detalle horas',
         'Id_nomina':'Id nomina',
         'Total':'Total',
         'Cantidad':'Cantidad',
        }
        widgets = {

        'Id_detalle_horas': forms.TextInput(attrs={'class':'form-control'}),
        'Id_nomina': forms.TextInput(attrs={'class':'form-control'}),
        'Total': forms.TextInput(attrs={'class':'form-control'}),
        'Cantidad': forms.TextInput(attrs={'class':'form-control'}),
        }

class Horas_extrasForm(forms.ModelForm):
    class Meta:

        model= Horas_extras

        fields = [

        'Id_horas_extras',
        'Nombre',
        'Valor_hora_extra',
        'Estado',
        'Id_detalle_horas',
        ]

        labels = {

        'Id_horas_extras':'Id horas extras',
        'Nombre':'Nombre',
        'Valor_hora_extra':'Valor hora extra',
        'Estado':'Estado',
        'Id_detalle_horas':'Id datelle horas',
        }
        widgets = {

        'Id_horas_extras': forms.TextInput(attrs={'class':'form-control'}),
        'Nombre': forms.TextInput(attrs={'class':'form-control'}),
        'Valor_hora_extra': forms.TextInput(attrs={'class':'form-control'}),
        'Estado': forms.TextInput(attrs={'class':'form-control'}),
        'Id_detalle_horas': forms.TextInput(attrs={'class':'form-control'}),
        }

class NominaForm(forms.ModelForm):
    class Meta:

        model= Nomina

        fields = [

        'Id_nomina',
        'Valor_pagar',
        'Subtotal',
        'Id_periodo',
        'Id_empleado',
        'Pago',
        'Estado',
        ]

        labels = {

        'Id_nomina':'Id nomina',
        'Valor_pagar':'Valor pagar',
        'Subtotal':'Subtotal',
        'Id_periodo':'Id periodo',
        'Id_empleado':'Id empleado',
        'Pago':'Pago',
        'Estado':'Estado',
        }
        widgets = {

        'Id_nomina': forms.TextInput(attrs={'class':'form-control'}),
        'Valor_pagar': forms.TextInput(attrs={'class':'form-control'}),
        'Subtotal': forms.TextInput(attrs={'class':'form-control'}),
        'Id_periodo': forms.TextInput(attrs={'class':'form-control'}),
        'Id_empleado': forms.TextInput(attrs={'class':'form-control'}),
        'Pago': forms.TextInput(attrs={'class':'form-control'}),
        'Estado': forms.TextInput(attrs={'class':'form-control'}),
        }

class PeriodoForm(forms.ModelForm):
    class Meta:

        model= Periodo

        fields = [

        'Id_periodo',
        'Anual',
        'Mes',
        ]

        labels = {

        'Id_periodo':'Id periodo',
        'Anual':'Anual - DD/MM/AAAA',
        'Mes':'Mes - DD/MM/AAAA',
        }
        widgets = {

        'Id_periodo': forms.TextInput(attrs={'class':'form-control'}),
        'Anual':  forms.widgets.DateInput(format='%Y-%m-%d', attrs={'id':"id",'value':datetime.now().strftime('%Y-%m-%d'),'type':'date', 'class':'form-control'}),
        'Mes':  forms.widgets.DateInput(format='%Y-%m-%d', attrs={'id':"id",'value':datetime.now().strftime('%Y-%m-%d'),'type':'date', 'class':'form-control'}),
        }
