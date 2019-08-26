// Edit datatable for patients

$(document).ready( function () {
    $('#edit_patient_dt').DataTable({
        language: {url: "//cdn.datatables.net/plug-ins/a5734b29083/i18n/Spanish.json"},
        scrollY:        "400px",
        scrollCollapse: true,
        paging:         false,
        autoWidth: true,
    } );
} );