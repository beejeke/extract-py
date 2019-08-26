// MREM chart for CAMDEX data visualization

$('#mrem_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/mrem";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('mrem_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-mrem-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('mrem_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');