// Patients information datatable

$(document).ready( function () {
    $('#camdex_patient').DataTable({
        language: {url: "//cdn.datatables.net/plug-ins/a5734b29083/i18n/Spanish.json"},
        pageLength: 5,
        scrollY: '45vh',
        scrollCollapse: true,
        autoWidth: true,
        paging: false,
        searching: false,
    } );
} );