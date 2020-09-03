from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.platypus.tables import Table, TableStyle

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.administrar_nomina.form import CargoForm, Tipo_vinculacionForm, EmpleadoForm, ParafiscalesForm, Detalle_parafiscalesForm, Reporte_horasForm, Detalle_horasForm, Horas_extrasForm, NominaForm, PeriodoForm
from apps.administrar_nomina.models import Cargo, Tipo_vinculacion, Empleado, Parafiscales, Periodo, Nomina, Detalle_parafiscales, Reporte_horas, Detalle_horas, Horas_extras

from django.contrib import messages
from itertools import chain

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return render (request, 'administrar_nomina/index.html')

class ReportecargosPDF(View):
    def cabecera(self,pdf):
        archivo_imagen = settings.MEDIA_ROOT+'file:///C:/proyectosDjango/nomipro22/static/images/logo_django.png'
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"PYTHON REPORTE")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE CARGOS")

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf,y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


    def tabla(self, pdf, y):
        encabezados = (
            'Id_cargo',
            'Nombre',
            'Estado',
            'Valor_cargo' 
        )

        Cargos = [(

            Cargo.Id_cargo,
            Cargo.Nombre,
            Cargo.Estado,
            Cargo.Valor_cargo
        )
        for Cargo in Cargo.objects.all()]
        Cargo_orden = Table([encabezados] + Cargos, colWidths=[2*cm, 2*cm, 2*cm, 3*cm ])
        Cargo_orden.setStyle(TableStyle(
            [
                ('ALING', (0,0),(3,0), 'CENTER'),
                ('GRID', (0,0),(-1,-1), (1), colors.black),
                ('FONTSIZE', (0,0),(-1,-1), 10),
            ]
        ))

        Cargo_orden.wrapOn(pdf,800,600)
        Cargo_orden.drawOn(pdf,60,y)




class CargoList(ListView):
    model=Cargo
    context_object_name='obj'
    template_name='administrar_nomina/Cargo_list.html'
    
class Tipo_vinculacionList(ListView):
    model=Tipo_vinculacion
    template_name='administrar_nomina/Tipo_vinculacion_list.html'

class EmpleadoList(ListView):
    model=Empleado
    template_name='administrar_nomina/Empleado_list.html'

class ParafiscalesList(ListView):
    model=Parafiscales
    template_name='administrar_nomina/Parafiscales_list.html'

class PeriodoList(ListView):
    model=Periodo
    template_name='administrar_nomina/Periodo_list.html'

class NominaList(ListView):
    model=Nomina
    template_name='administrar_nomina/Nomina_list.html'

class Detalle_parafiscalesList(ListView):
    model=Detalle_parafiscales
    template_name='administrar_nomina/Detalle_parafiscales_list.html'

class Reporte_horasList(ListView):
    model=Reporte_horas
    template_name='administrar_nomina/Reporte_horas_list.html'

class Detalle_horasList(ListView):
    model=Detalle_horas
    template_name='administrar_nomina/Detalle_horas_list.html'

class Horas_extrasList(ListView):
    model=Horas_extras
    template_name='administrar_nomina/Horas_extras_list.html'



class CargoCreate(SuccessMessageMixin,CreateView):
    model=Cargo
    form_class=CargoForm
    template_name='administrar_nomina/Cargo_form.html'
    success_url= reverse_lazy('Cargo_lista')
    success_message = 'Cargo creado de manera exitosa'
    # fields = "__all__"

class Tipo_vinculacionCreate(SuccessMessageMixin,CreateView):
    model=Tipo_vinculacion
    form_class=Tipo_vinculacionForm
    template_name='administrar_nomina/Tipo_vinculacion_form.html'
    success_url= reverse_lazy('Tipo_vinculacion_lista')
    success_message = 'Tipo vinculacion creado de manera exitosa'

class EmpleadoCreate(SuccessMessageMixin,CreateView):
    model=Empleado
    form_class=EmpleadoForm
    template_name='administrar_nomina/Empleado_form.html'
    success_url= reverse_lazy('Empleado_lista')
    success_message = 'Empleado creado de manera exitosa'

class ParafiscalesCreate(SuccessMessageMixin,CreateView):
    model=Parafiscales
    form_class=ParafiscalesForm
    template_name='administrar_nomina/Parafiscales_form.html'
    success_url= reverse_lazy('Parafiscales_lista')
    success_message = 'Parafiscales creado de manera exitosa'

class PeriodoCreate(SuccessMessageMixin,CreateView):
    model=Periodo
    form_class=PeriodoForm
    template_name='administrar_nomina/Periodo_form.html'
    success_url= reverse_lazy('Periodo_lista')
    success_message = 'Periodo creado de manera exitosa'

class NominaCreate(SuccessMessageMixin,CreateView):
    model=Nomina
    form_class=NominaForm
    template_name='administrar_nomina/Nomina_form.html'
    success_url= reverse_lazy('Nomina_lista')
    success_message = 'Nomina creado de manera exitosa'
    context_object_name='obj'

    def get_context_data(self,**kwargs):
        context = super(NominaCreate,self).get_context_data(**kwargs)
        context['form2'] = Detalle_parafiscales.objects.all()
        context['form3'] = Detalle_horas.objects.all()
        context['form4'] = Parafiscales.objects.all()
        context['form5'] = Horas_extras.objects.all()
        context['form6'] = Cargo.objects.all()
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if request.method=='POST':
            if form.is_valid():
                Nomina = form.save(commit=False)
                Nomina.Valor_pagar = request.POST.get("id_Valor_pagar2")
                Nomina.Subtotal = request.POST.get("id_Subtotal")
                Nomina.Total = request.POST.get("id_Total")
                Nomina = form.save()
                Nomina.save()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.render_to_response(self.get_context_data(form=form))

class Detalle_parafiscalesCreate(SuccessMessageMixin,CreateView):
    model=Detalle_parafiscales
    form_class=Detalle_parafiscalesForm
    template_name='administrar_nomina/Detalle_parafiscales_form.html'
    success_url= reverse_lazy('Detalle_parafiscales_lista')
    success_message = 'Detalle parafiscales creado de manera exitosa'

class Reporte_horasCreate(SuccessMessageMixin,CreateView):
    model=Reporte_horas
    form_class=Reporte_horasForm
    template_name='administrar_nomina/Reporte_horas_form.html'
    success_url= reverse_lazy('Reporte_horas_lista')
    success_message = 'Reporte horas creado de manera exitosa'

class Detalle_horasCreate(SuccessMessageMixin,CreateView):
    model=Detalle_horas
    form_class=Detalle_horasForm
    template_name='administrar_nomina/Detalle_horas_form.html'
    success_url= reverse_lazy('Detalle_horas_lista')
    success_message = 'Detalle horas creado de manera exitosa'

class Horas_extrasCreate(SuccessMessageMixin,CreateView):
    model=Horas_extras
    form_class=Horas_extrasForm
    template_name='administrar_nomina/Horas_extras_form.html'
    success_url= reverse_lazy('Horas_extras_lista')
    success_message = 'Horas extras creado de manera exitosa'



class CargoUpdate(SuccessMessageMixin,UpdateView):
    model=Cargo
    form_class=CargoForm
    template_name='administrar_nomina/Cargo_form.html'
    success_url= reverse_lazy('Cargo_lista')
    success_message = 'Cargo editado de manera exitosa'

class Tipo_vinculacionUpdate(SuccessMessageMixin,UpdateView):
    model=Tipo_vinculacion
    form_class=Tipo_vinculacionForm
    template_name='administrar_nomina/Tipo_vinculacion_form.html'
    success_url= reverse_lazy('Tipo_vinculacion_lista')
    success_message = 'Tipo vinculacion editado de manera exitosa'

class EmpleadoUpdate(SuccessMessageMixin,UpdateView):
    model=Empleado
    form_class=EmpleadoForm
    template_name='administrar_nomina/Empleado_form.html'
    success_url= reverse_lazy('Empleado_lista')
    success_message = 'Empleado editado de manera exitosa'

class ParafiscalesUpdate(SuccessMessageMixin,UpdateView):
    model=Parafiscales
    form_class=ParafiscalesForm
    template_name='administrar_nomina/Parafiscales_form.html'
    success_url= reverse_lazy('Parafiscales_lista')
    success_message = 'Parafiscales editado de manera exitosa'

class PeriodoUpdate(SuccessMessageMixin,UpdateView):
    model=Periodo
    form_class=PeriodoForm
    template_name='administrar_nomina/Periodo_form.html'
    success_url= reverse_lazy('Periodo_lista')
    success_message = 'Periodo editado de manera exitosa'

class NominaUpdate(SuccessMessageMixin,UpdateView):
    model=Nomina
    form_class=NominaForm
    template_name='administrar_nomina/Nomina_form.html'
    success_url= reverse_lazy('Nomina_lista')
    success_message = 'Nomina editado de manera exitosa'

class Detalle_parafiscalesUpdate(SuccessMessageMixin,UpdateView):
    model=Detalle_parafiscales
    form_class=Detalle_parafiscalesForm
    template_name='administrar_nomina/Detalle_parafiscales_form.html'
    success_url= reverse_lazy('Detalle_parafiscales_lista')
    success_message = 'Detalle parafiscales editado de manera exitosa'

class Reporte_horasUpdate(SuccessMessageMixin,UpdateView):
    model=Reporte_horas
    form_class=Reporte_horasForm
    template_name='administrar_nomina/Reporte_horas_form.html'
    success_url= reverse_lazy('Reporte_horas_lista')
    success_message = 'Reporte horas editado de manera exitosa'

class Detalle_horasUpdate(SuccessMessageMixin,UpdateView):
    model=Detalle_horas
    form_class=Detalle_horasForm
    template_name='administrar_nomina/Detalle_horas_form.html'
    success_url= reverse_lazy('Detalle_horas_lista')
    success_message = 'Detalle horas editado de manera exitosa'

class Horas_extrasUpdate(SuccessMessageMixin,UpdateView):
    model=Horas_extras
    form_class=Horas_extrasForm
    template_name='administrar_nomina/Horas_extras_form.html'
    success_url= reverse_lazy('Horas_extras_lista')
    success_message = 'Horas extras editado de manera exitosa'


class CargoDelete(DeleteView):
    model=Cargo
    template_name='administrar_nomina/Cargo_delete.html'
    success_url= reverse_lazy('Cargo_lista')
    success_message = 'Cargo eliminado de manera exitosa'

class Tipo_vinculacionDelete(DeleteView):
    model=Tipo_vinculacion
    template_name='administrar_nomina/Tipo_vinculacion_delete.html'
    success_url= reverse_lazy('Tipo_vinculacion_lista')
    success_message = 'Tipo vinculacion eliminado de manera exitosa'

class EmpleadoDelete(DeleteView):
    model=Empleado
    template_name='administrar_nomina/Empleado_delete.html'
    success_url= reverse_lazy('Empleado_lista')
    success_message = 'Empleado eliminado de manera exitosa'

class ParafiscalesDelete(DeleteView):
    model=Parafiscales
    template_name='administrar_nomina/Parafiscales_delete.html'
    success_url= reverse_lazy('Parafiscales_lista')
    success_message = 'Parafiscal eliminado de manera exitosa'

class PeriodoDelete(DeleteView):
    model=Periodo
    template_name='administrar_nomina/Periodo_delete.html'
    success_url= reverse_lazy('Periodo_lista')
    success_message = 'Perido eliminado de manera exitosa'

class NominaDelete(DeleteView):
    model=Nomina
    template_name='administrar_nomina/Nomina_delete.html'
    success_url= reverse_lazy('Nomina_lista')
    success_message = 'Nomina eliminada de manera exitosa'

class Detalle_parafiscalesDelete(DeleteView):
    model=Detalle_parafiscales
    template_name='administrar_nomina/Detalle_parafiscales_delete.html'
    success_url= reverse_lazy('Detalle_parafiscales_lista')
    success_message = 'Detalle parafiscal eliminado de manera exitosa'

class Reporte_horasDelete(DeleteView):
    model=Reporte_horas
    template_name='administrar_nomina/Reporte_horas_delete.html'
    success_url= reverse_lazy('Reporte_horas_lista')
    success_message = 'Reporte hora eliminada de manera exitosa'

class Detalle_horasDelete(DeleteView):
    model=Detalle_horas
    template_name='administrar_nomina/Detalle_horas_delete.html'
    success_url= reverse_lazy('Detalle_horas_lista')
    success_message = 'Detalle hora eliminada de manera exitosa'

class Horas_extrasDelete(DeleteView):
    model=Horas_extras
    template_name='administrar_nomina/Horas_extras_delete.html'
    success_url= reverse_lazy('Horas_extras_lista')
    success_message = 'Hora extra eliminada de manera exitosa'


class CargoDetalle(DetailView):
    model=Cargo
    template_name='administrar_nomina/Cargo_detalle.html'

class Tipo_vinculacionDetalle(DetailView):
    model=Tipo_vinculacion
    template_name='administrar_nomina/Tipo_vinculacion_detalle.html'

class EmpleadoDetalle(DetailView):
    model=Empleado
    template_name='administrar_nomina/Empleado_detalle.html'

class ParafiscalesDetalle(DetailView):
    model=Parafiscales
    template_name='administrar_nomina/Parafiscales_detalle.html'

class PeriodoDetalle(DetailView):
    model=Periodo
    template_name='administrar_nomina/Periodo_detalle.html'

class NominaDetalle(DetailView):
    model=Nomina
    template_name='administrar_nomina/Nomina_detalle.html'

class Detalle_parafiscalesDetalle(DetailView):
    model=Detalle_parafiscales
    template_name='administrar_nomina/Detalle_parafiscales_detalle.html'

class Reporte_horasDetalle(DetailView):
    model=Reporte_horas
    template_name='administrar_nomina/Reporte_horas_detalle.html'

class Detalle_horasDetalle(DetailView):
    model=Detalle_horas
    template_name='administrar_nomina/Detalle_horas_detalle.html'

class Horas_extrasDetalle(DetailView):
    model=Horas_extras
    template_name='administrar_nomina/Horas_extras_detalle.html'


