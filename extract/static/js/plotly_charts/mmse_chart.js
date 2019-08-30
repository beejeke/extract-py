// MMSE chart for CAMDEX data visualization

$('#mmse_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/mmse";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('mmse_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-others-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('mmse_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');