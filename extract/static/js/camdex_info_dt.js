// Patients information datatable

$(document).ready( function () {
    $('#camdex_patient').DataTable({
        language: {url: "//cdn.datatables.net/plug-ins/a5734b29083/i18n/Spanish.json"},
        pageLength: 5,
        scrollX: false,
        scrollY: '45vh',
        scrollCollapse: true,
        autoWidth: true,
        paging: false,
        searching: false,
        ordering: false,
        processing: true,
        serverSide: true,
        ajax: {
            url: "/patients/" + $('#patient').val(),
            data: function(data) {
                data.patient = $('#patient').val();
            }
        },
        columns: [
            { data: "name" },
            { data: "address" },
            { data: "phone" },
            { data: "email" },
            { data: "age" },
            { data: "dni" },
            { data: "birthdate" },
        ]
    } );

    $('#patient').on('change', function() {
        var table = $('#camdex_patient').DataTable();
        table.ajax.url("/patients/" + $('#patient').val());
        table.ajax.reload();
    } );
} );