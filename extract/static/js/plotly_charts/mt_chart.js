// MT chart for CAMDEX data visualization

$('#mt_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/mt";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('mt_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-mem-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('mt_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');