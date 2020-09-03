from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.administrar_nomina.views import index, CargoCreate, Tipo_vinculacionCreate,  EmpleadoCreate, ParafiscalesCreate, Detalle_parafiscalesCreate,\
     Reporte_horasCreate, Detalle_horasCreate, Horas_extrasCreate, NominaCreate, PeriodoCreate,\
         CargoUpdate, Tipo_vinculacionUpdate, EmpleadoUpdate,ParafiscalesUpdate, PeriodoUpdate, NominaUpdate, Detalle_parafiscalesUpdate, Reporte_horasUpdate, Horas_extrasUpdate, Detalle_horasUpdate,\
         CargoDelete, Tipo_vinculacionDelete, EmpleadoDelete, ParafiscalesDelete, PeriodoDelete, NominaDelete, Detalle_parafiscalesDelete, Reporte_horasDelete, Detalle_horasDelete,Horas_extrasDelete,\
         CargoList, Tipo_vinculacionList, EmpleadoList, ParafiscalesList, PeriodoList, NominaList, Detalle_parafiscalesList, Reporte_horasList, Detalle_horasList, Horas_extrasList,\
             CargoDetalle, Detalle_horasDetalle,Tipo_vinculacionDetalle,EmpleadoDetalle, ParafiscalesDetalle, PeriodoDetalle, NominaDetalle, Detalle_parafiscalesDetalle, Reporte_horasDetalle, Horas_extrasDetalle, ReportecargosPDF

urlpatterns= [
    url(r'^$', index, name='index'),
    url(r'^Cargo$', login_required (CargoCreate.as_view()), name='Cargo_crear'),
    url(r'^Tipo_vinculacion$', login_required (Tipo_vinculacionCreate.as_view()), name='Tipo_vinculacion_crear'),
    url(r'^Empleado$', login_required (EmpleadoCreate.as_view()), name='Empleado_crear'),
    url(r'^Parafiscales$', login_required (ParafiscalesCreate.as_view()), name='Parafiscales_crear'),
    url(r'^Periodo$',login_required (PeriodoCreate.as_view()), name='Periodo_crear'),
    url(r'^Nomina$',login_required (NominaCreate.as_view()), name='Nomina_crear'),
    url(r'^Detalle_parafiscales$',  login_required (Detalle_parafiscalesCreate.as_view()), name='Detalle_parafiscales_crear'),
    url(r'^Reporte_horas$',login_required (Reporte_horasCreate.as_view()), name='Reporte_horas_crear'),
    url(r'^Detalle_horas$',login_required (Detalle_horasCreate.as_view()), name='Detalle_horas_crear'),
    url(r'^Horas_extras$',login_required (Horas_extrasCreate.as_view()), name='Horas_extras_crear'),
    

    url(r'^Cargolista$',login_required (CargoList.as_view()), name='Cargo_lista'),
    url(r'^Tipo_vinculacionlista$',login_required (Tipo_vinculacionList.as_view()), name='Tipo_vinculacion_lista'),
    url(r'^Empleadolista$',login_required (EmpleadoList.as_view()), name='Empleado_lista'),
    url(r'^Parafiscaleslista$',login_required (ParafiscalesList.as_view()), name='Parafiscales_lista'),
    url(r'^Periodolista$',login_required (PeriodoList.as_view()), name='Periodo_lista'),
    url(r'^Nominalista$',login_required (NominaList.as_view()), name='Nomina_lista'),
    url(r'^Detalle_parafiscaleslista$',login_required (Detalle_parafiscalesList.as_view()), name='Detalle_parafiscales_lista'),
    url(r'^Reporte_horaslista$',login_required (Reporte_horasList.as_view()), name='Reporte_horas_lista'),
    url(r'^Detalle_horaslista$',login_required (Detalle_horasList.as_view()), name='Detalle_horas_lista'),
    url(r'^Horas_extraslista$',login_required (Horas_extrasList.as_view()), name='Horas_extras_lista'),


    url(r'^editarcargo/(?P<pk>\d+)/$',login_required (CargoUpdate.as_view()), name='Cargo_editar'),
    url(r'^editartipo_vinculacion/(?P<pk>\d+)/$',login_required (Tipo_vinculacionUpdate.as_view()), name='Tipo_vinculacion_editar'),
    url(r'^editarempleado/(?P<pk>\d+)/$',login_required (EmpleadoUpdate.as_view()), name='Empleado_editar'),
    url(r'^editarparafiscales/(?P<pk>\d+)/$',login_required (ParafiscalesUpdate.as_view()), name='Parafiscales_editar'),
    url(r'^editarperiodo/(?P<pk>\d+)/$',login_required (PeriodoUpdate.as_view()), name='Periodo_editar'),
    url(r'^editarnomina/(?P<pk>\d+)/$',login_required (NominaUpdate.as_view()), name='Nomina_editar'),
    url(r'^editardetalle_parafiscales/(?P<pk>\d+)/$',login_required (Detalle_parafiscalesUpdate.as_view()), name='Detalle_parafiscales_editar'),
    url(r'^editarreporte_horas/(?P<pk>\d+)/$',login_required (Reporte_horasUpdate.as_view()), name='Reporte_horas_editar'),
    url(r'^editardetalle_horas/(?P<pk>\d+)/$',login_required (Detalle_horasUpdate.as_view()), name='Detalle_horas_editar'),
    url(r'^editarhoras_extras/(?P<pk>\d+)/$',login_required (Horas_extrasUpdate.as_view()), name='Horas_extras_editar'),
    

    url(r'^eliminarcargo/(?P<pk>\d+)/$',login_required (CargoDelete.as_view()), name='Cargo_eliminar'),
    url(r'^eliminartipo_vinculacion/(?P<pk>\d+)/$',login_required (Tipo_vinculacionDelete.as_view()), name='Tipo_vinculacion_eliminar'),
    url(r'^eliminarempleado/(?P<pk>\d+)/$',login_required (EmpleadoDelete.as_view()), name='Empleado_eliminar'),
    url(r'^eliminarparafiscales/(?P<pk>\d+)/$',login_required (ParafiscalesDelete.as_view()), name='Parafiscales_eliminar'),
    url(r'^eliminarperiodo/(?P<pk>\d+)/$',login_required (PeriodoDelete.as_view()), name='Periodo_eliminar'),
    url(r'^eliminarnomina/(?P<pk>\d+)/$',login_required (NominaDelete.as_view()), name='Nomina_eliminar'),
    url(r'^eliminardetalle_parafiscales/(?P<pk>\d+)/$',login_required (Detalle_parafiscalesDelete.as_view()), name='Detalle_parafiscales_eliminar'),
    url(r'^eliminarreporte_horas/(?P<pk>\d+)/$',login_required (Reporte_horasDelete.as_view()), name='Reporte_horas_eliminar'),
    url(r'^eliminardetalle_horas/(?P<pk>\d+)/$',login_required (Detalle_horasDelete.as_view()), name='Detalle_horas_eliminar'),
    url(r'^eliminarhoras_extras/(?P<pk>\d+)/$',login_required (Horas_extrasDelete.as_view()), name='Horas_extras_eliminar'),


    url(r'^detallecargo/(?P<pk>\d+)/$',login_required (CargoDetalle.as_view()), name='Cargo_detalle'),
    url(r'^detalletipo_vinculacion/(?P<pk>\d+)/$',login_required (Tipo_vinculacionDetalle.as_view()), name='Tipo_vinculacion_detalle'),
    url(r'^detalleempleado/(?P<pk>\d+)/$',login_required (EmpleadoDetalle.as_view()), name='Empleado_detalle'),
    url(r'^detalleparafiscales/(?P<pk>\d+)/$',login_required (ParafiscalesDetalle.as_view()), name='Parafiscales_detalle'),
    url(r'^detalleperiodo/(?P<pk>\d+)/$',login_required (PeriodoDetalle.as_view()), name='Periodo_detalle'),
    url(r'^detallenomina/(?P<pk>\d+)/$',login_required (NominaDetalle.as_view()), name='Nomina_detalle'),
    url(r'^detalledetalle_parafiscales/(?P<pk>\d+)/$',login_required (Detalle_parafiscalesDetalle.as_view()), name='Detalle_parafiscales_detalle'),
    url(r'^detallereporte_horas/(?P<pk>\d+)/$',login_required (Reporte_horasDetalle.as_view()), name='Reporte_horas_detalle'),
    url(r'^detalledetalle_horas/(?P<pk>\d+)/$',login_required (Detalle_horasDetalle.as_view()), name='Detalle_horas_detalle'),
    url(r'^detallehoras_extras/(?P<pk>\d+)/$',login_required (Horas_extrasDetalle.as_view()), name='Horas_extras_detalle'),




    url(r'^reporte_cargos_pdf/$',ReportecargosPDF.as_view(), name='reporte_cargos_pdf'),
]