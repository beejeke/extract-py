// MEC chart for CAMDEX data visualization

$('#mec_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/mec";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('mec_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-mec-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('mec_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');