// CAMDEX datatable for patients

$(document).ready( function () {
    $('#camdex').DataTable({
        language: {url: "//cdn.datatables.net/plug-ins/a5734b29083/i18n/Spanish.json"},
        pageLength: 10,
        scrollX: true,
        scrollY: '45vh',
        scrollCollapse: true,
        autoWidth: true,
        paging: false,
        searching: false,
    } );
} );