// CAMDEX datatable for patients

$(document).ready( function () {
    $('#camdex').DataTable({
        language: {url: "//cdn.datatables.net/plug-ins/a5734b29083/i18n/Spanish.json"},
        pageLength: 5,
        scrollX: true,
        scrollY: '45vh',
        scrollCollapse: true,
        autoWidth: true,
        paging: false,
        ordering: false,
        searching: false,
        processing: true,
        serverSide: true,
        ajax: {
            url: "/camdex/" + $('#patient').val(),
            data: function(data) {
                data.patient = $('#patient').val();
            }
        },
        columns: [
            { data: "mmse", width: "50%"  },
            { data: "mec", width: "50%"  },
            { data: "ryh", width: "50%"  },
            { data: "ct", width: "50%"  },
            { data: "ori", width: "50%"  },
            { data: "lt", width: "50%"  },
            { data: "lc", width: "50%"  },
            { data: "lp", width: "50%"  },
            { data: "mt", width: "50%"  },
            { data: "mrec", width: "50%"  },
            { data: "mrem", width: "50%"  },
            { data: "ma", width: "50%"  },
            { data: "ac", width: "50%"  },
            { data: "pr", width: "50%"  },
            { data: "cal", width: "50%"  },
            { data: "pabs", width: "50%"  },
            { data: "ptv", width: "50%"  },
        ]
    } );

    $('#patient').on('change', function() {
        var table = $('#camdex').DataTable();
        table.ajax.url("/camdex/" + $('#patient').val());
        table.ajax.reload();
    } );
} );