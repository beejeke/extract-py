// PTV chart for CAMDEX data visualization

$('#ptv_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/ptv";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('ptv_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-ptv-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('ptv_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');