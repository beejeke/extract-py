// LT chart for CAMDEX data visualization

$('#lt_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/lt";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('lt_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-leng-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('lt_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');