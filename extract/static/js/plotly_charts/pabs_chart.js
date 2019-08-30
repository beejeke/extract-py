// PABS chart for CAMDEX data visualization

$('#pabs_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/pabs";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('pabs_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-others-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('pabs_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');