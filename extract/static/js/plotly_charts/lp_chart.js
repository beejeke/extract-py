// LP chart for CAMDEX data visualization

$('#lp_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/lp";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('lp_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-lp-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('lp_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');