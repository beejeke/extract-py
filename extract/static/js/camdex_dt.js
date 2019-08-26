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
            { data: "mmse" },
            { data: "mec" },
            { data: "ryh"  },
            { data: "ct"  },
            { data: "ori"  },
            { data: "lt"  },
            { data: "lc"  },
            { data: "lp"  },
            { data: "mt"  },
            { data: "mrec"  },
            { data: "mrem"  },
            { data: "ma"  },
            { data: "ac"  },
            { data: "pr"  },
            { data: "cal"  },
            { data: "pabs"  },
            { data: "ptv"  },
        ]
    } );

    $('#patient').on('change', function() {
        var table = $('#camdex').DataTable();
        table.ajax.url("/camdex/" + $('#patient').val());
        table.ajax.reload();
    } );
} );