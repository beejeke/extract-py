// CT chart for CAMDEX data visualization

$('#ct_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/ct";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('ct_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-ct-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('ct_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');