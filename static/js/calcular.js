// $(function () {

//     $('.select2').select2({
//         theme: "bootstrap4",
//         language: 'es'
//     });

//     $('#id').datepicker({
//         format: 'YYYY-MM-DD',
//         date: moment().format("YYYY-MM-DD"),
//         locale: 'es',
//         //minDate: moment().format("YYYY-MM-DD")
//     });
// });
// function PruebaInicial()
// {
//     alert("Probando ..");
// }
// function Calcular()
// {
//     var cant, prec, desc, iva, stotal, total;
//     new Intl.NumberFormat([locales [prec]])
//     cant = $("#id_cantidad").val();
//     cant = cant===""? 0 :+cant;
//     cant = cant<0 ? 0: cant;
    
//     prec = $("#id_precio").val();
//     prec = prec===""? 0 :+prec;
//     prec = prec<0 ? 0: prec;

//     desc = $("#id_descuento").val();
//     desc = desc===""? 0 :+desc;
//     desc = desc<0 ? 0: desc;

//     iva = $("#id_iva").val();
//     iva = iva===""? 0 :+iva;
//     iva = iva<0 ? 0: iva;

//     desc = desc>(cant*prec) ? 0:desc;

//     stotal = cant * prec;
//     iva = (stotal-desc)*(iva/100)
//     total = (stotal-desc)+iva;

//     $('#id_cantidad').val(cant);
//     $('#id_precio').val(prec);
//     $('#id_descuento').val(desc);
//     $('#id_iva').val(iva);

//     $('#id_subtotal').val(stotal);
//     $('#id_total').val(total);

// }

// function PruebaInicial()
//  {
//     alert("Probando ..");
//  }

//  function Prueba()
//  {
//      var  valcargo, canthoras, horaex, subtotal,valparafis, parafis, totalpag ;
     

//      valcargo = $("#id_Valor_cargo").val();
//      valcargo = valcargo===""? 0 :+valcargo;
//      valcargo = valcargo<0 ? 0: valcargo;

//      canthoras = $("#id_cantidad_horas_extras").val();
//      canthoras = canthoras===""? 0 :+canthoras;
//      canthoras = canthoras<0 ? 0: canthoras;

//      horaex = $("#id_horas_extras").val();
//      horaex = horaex===""? 0 :+horaex;
//      horaex = horaex<0 ? 0: horaex;

//      subtotal = $("#id_subtotal").val();
//      subtotal = subtotal===""? 0 :+subtotal;
//      subtotal = subtotal<0 ? 0: subtotal;

//      valparafis = $("#id_valor_parafiscales").val();
//      valparafis = valparafis===""? 0 :+valparafis;
//      valparafis = valparafis<0 ? 0: valparafis;

//      parafis = $("#id_parafiscales").val();
//      parafis = parafis===""? 0 :+parafis;
//      parafis = parafis<0 ? 0: parafis;

//      totalpag = $("#id_Total_pago").val();
//      totalpag = totalpag===""? 0 :+totalpag;
//      totalpag = totalpag<0 ? 0: totalpag;

//      horaex = canthoras * (4135);
//      subtotal = valcargo + horaex;
//      parafis = subtotal*(valparafis/100);
//      totalpag = horaex + parafis;


//      $('#id_valor_cargo').val(valcargo);
//      $('#id_cantidad_horas_extras').val(canthoras);
//      $('#id_horas_extras').val(horaex);
//      $('#id_subtotal').val(subtotal);
//      $('#id_valor_parafiscales').val(valparafis);
//      $('#id_parafiscales').val(parafis);
//      $('#id_Total_pago').val(totalpag);


//  }

 function Calcular() {

    var nombre_parafiscal,nombre_extras, valpagar, valpagar2, parafiscal,subtotal,total,cant_horas,horas_extras;
  
    nombre_parafiscal=$("#id_nombre_parafiscal").val();
    nombre_extras=$("#id_nombre_extras").val();

    parafiscal=$("#id_parafiscales").val();
  
    
    cant_horas=$("#id_cantidad_horas").val();
    cant_horas = parseFloat(cant_horas)
   
    horas_extras=$("#id_horas").val();
    horas_extras = (parseInt(horas_extras)/100);
 
    valpagar=$("#id_Valor_pagar2").val();
    valpagar = parseInt(valpagar)
   
    subtotal= (valpagar/240)*(horas_extras*(parseInt(cant_horas)))+valpagar;
    
    parafiscal  = (parseInt(parafiscal)) * valpagar;
   
    
    total= (subtotal - parafiscal) ;
    subtotal= parseFloat(subtotal);
    total = parseFloat(total);
    valpagar = parseFloat(valpagar);
 
    $('#id_nombre_extras').val(nombre_extras);
    $('#id_parafiscales').val(parafiscal);
    $('#id_nombre_parafiscal').val(nombre_parafiscal);
    $('#id_Subtotal').val(subtotal);
    $('#id_cantidad_horas').val(cant_horas);
    $('#id_horas').val(horas_extras);
    //$('#id_valorpagar').val(valpagar);
    $('#id_Valor_pagar2').val(valpagar);
    $('#id_Total').val(total);
    //$('#id_nomina').val(id_nomina);
    alert('el salario del empleado es :' + valpagar);
    alert('horas que se le pagana al empleado:' + horas_extras);
    alert('subotal :' + subtotal);
    alert('total a pagar es de :' + total);
    
  

} 